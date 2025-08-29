"""
Core document generation logic for gcdocs
Refactored from the Report class in original datamodel.py
"""

import json
import pandas as pd
import os
import re
import sys
import yaml

from pathlib import Path
from typing import Dict, Any, List, Optional
from collections import OrderedDict
from loguru import logger
import subprocess
import datetime
import babel.dates

from ..config import GeoDataConfig
from ..translation.translator import SimpleTranslator, create_translator

def get_short_revision(version_str):
    parts = version_str.split(".")
    digits = []

    for part in parts:
        if part.isdigit():
            digits.append(int(part))
        if len(digits) == 2:
            break

    if len(digits) < 2:
        raise ValueError(f"Not enough significant digits in version string: '{version_str}'")

    return ".".join(map(str, digits))

def get_git_revision_info():
    """Get git revision info and determine if this is a release version."""
    try:
        # Get short hash
        hash_short = (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
            .decode("ascii")
            .strip()
        )

        # Check if current commit is tagged (indicates release)
        try:
            tag = (
                subprocess.check_output(
                    ["git", "describe", "--exact-match", "--tags", "HEAD"],
                    stderr=subprocess.DEVNULL,
                )
                .decode("ascii")
                .strip()
            )
            is_release = True
        except subprocess.CalledProcessError:
            is_release = False
            tag = None

        return {"hash": hash_short, "is_release": is_release, "tag": tag}
    except subprocess.CalledProcessError:
        return {"hash": "unknown", "is_release": False, "tag": None}


class MarkdownGenerator:
    """Main document generator (refactored from Report class)"""

    def __init__(self, config: Optional[GeoDataConfig] = None):
        self.config = config or GeoDataConfig()
        self._model: Optional[Dict[str, Any]] = None
        self._prefixes: List[str] = []
        self._classnames: List[str] = []
        self._translator: Optional[SimpleTranslator] = None

    def load_model(self, config_file: str) -> Dict[str, Any]:
        """Load YAML datamodel (replaces model property)"""
        if self._model is None:
            with open(config_file, "rt", encoding="utf8") as f:
                self._model = yaml.load(f, Loader=yaml.FullLoader)

            # Add metadata
            from datetime import date
            import subprocess

            self._model["date"] = str(date.today())
            model = self._model.get("model")
            if model:
                revision = model.get("revision")
                short_revision = get_short_revision(revision)
                self._model['model']['short_revision'] = short_revision

            self._model["date"] = str(datetime.date.today())

            self._model["git_info"] = get_git_revision_info()

            try:
                git_hash = (
                    subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
                    .decode("ascii")
                    .strip()
                )
                self._model["hash"] = git_hash
            except (subprocess.CalledProcessError, FileNotFoundError):
                self._model["hash"] = "unknown"

        return self._model

    @property
    def classnames(self) -> List[str]:
        if not self._classnames and self._model:
            classnames = []
            for theme in self._model.get("themes", []):
                try:
                    for cls in theme.get("classes", []):
                        classname = cls.get("name")
                        if classname:
                            classnames.append(classname)
                except (KeyError, TypeError, IndexError) as e:
                    logger.error(f"Error processing theme '{theme}': {e}")

            self._classnames = sorted(list(set(classnames)))
        return self._classnames

    @property
    def prefixes(self) -> List[str]:
        """Get all class prefixes (replaces prefixes property)"""
        if not self._prefixes and self._model:
            prefixes = []
            for theme in self._model.get("themes", []):
                try:
                    for cls in theme.get("classes", []):
                        cls_abrev = cls.get("abrev")
                        if cls_abrev:
                            prefixes.append(cls_abrev)
                except (KeyError, TypeError, IndexError) as e:
                    logger.error(f"Error processing theme '{theme}': {e}")

            self._prefixes = sorted(list(set(prefixes)))
        return self._prefixes

    def _get_translator(self) -> SimpleTranslator:
        """Get or create translator instance"""
        if self._translator is None:
            self._translator = create_translator(self.config.translation_df)
        return self._translator

    def _get_coded_values(self, domain_name: str) -> Dict[str, str]:
        """Get coded values from domain (from original get_coded_values function)"""
        domains = self.config.domains

        if domain_name in domains:
            domain = domains.get(domain_name)
            if domain.get("type") == "CodedValue":
                coded_values = domain.get("codedValues", {})

                # Handle special codes (from original custom_sort_key logic)
                if "999997" in coded_values:
                    coded_values["999997"] = "unbekannt"
                if "999998" in coded_values:
                    coded_values["999998"] = "nicht anwendbar"

                # Sort with special handling for 999997, 999998
                def sort_key(item):
                    key, _ = item
                    if key in ["999997", "999998"]:
                        return float("inf")
                    try:
                        return int(key)
                    except ValueError:
                        return float("inf")

                return dict(sorted(coded_values.items(), key=sort_key))

        return {}

    def _get_table_values(self, name: str) -> Dict[str, str]:
        """Get values from table files (from original get_table_values function)"""
        try:
            file_path = self.config.input_dir / f"{name}.json"

            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # Check if data is already a simple key-value dict (like your Admixture.json)
                if isinstance(data, dict) and all(isinstance(v, str) for v in data.values()):
                    # It's already a simple mapping, just return it
                    logger.debug(f"Loaded simple mapping from {file_path}: {len(data)} entries")
                    return data

                # If it's a list of records (like from database export)
                elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                    df = pd.DataFrame(data)

                    # Try to find the right columns
                    geol_code_col = None
                    german_col = None

                    for col in df.columns:
                        if "GEOL_CODE_INT" in col.upper():
                            geol_code_col = col
                        elif "GERMAN" in col.upper():
                            german_col = col

                    if geol_code_col and german_col:
                        df[geol_code_col] = df[geol_code_col].astype(str)
                        result = df.set_index(geol_code_col)[german_col].to_dict()
                        logger.debug(f"Loaded table data from {file_path}: {len(result)} entries")
                        return result
                    else:
                        logger.warning(f"Could not find GEOL_CODE_INT and GERMAN columns in {file_path}")
                        return {}

                # Fallback: try to convert whatever it is
                else:
                    logger.warning(f"Unexpected data format in {file_path}, returning empty dict")
                    return {}

            else:
                logger.warning(f"Table file not found: {file_path}")
                return {}

        except Exception as e:
            logger.error(f"Error loading table values from {name}: {e}")
            logger.debug(f"File path attempted: {self.config.input_dir / f'{name}.json'}")
            return {}

    def _get_subtype_values(self, value: str) -> Dict[str, str]:
        """Get subtype values (from original get_subtype function)"""
        subtypes = self.config.subtypes
        result = {}

        keys = [x for x in subtypes if str(x).startswith(str(value))]

        for key in keys:
            if key in subtypes:
                result[key] = subtypes[key]

        return result

    def _check_attribute_consistency(
        self,
        cls_name: str,
        table_name: str,
        attributes_in_model: List[str],
        cls_abrev: str,
    ):
        """Check model vs database consistency (from original check_attribute_in_table)"""
        # Simplified version - log warnings about missing attributes
        tables_dict = self.config.tables_dict
        table_full_name = f"TOPGIS_GC.{table_name.upper()}"

        if table_full_name not in tables_dict:
            logger.warning(f"Table {table_full_name} not found in schema")
            return

        # This is a simplified version - you can enhance based on your needs
        logger.debug(f"Checking consistency for {cls_name} against {table_name}")

    def process_model(self, model_file: str) -> Dict[str, Any]:
        """Process the datamodel file and enrich with database info (from original to_json method)"""
        model = self.load_model(model_file)
        translator = self._get_translator()

        logger.info(f"Processing model with prefixes: {self.prefixes}")

        # Process themes and classes
        for theme in model.get("themes", []):
            theme_name = theme.get("name", "")
            if not theme_name:
                logger.error("Missing theme name")
                continue

            for cls in theme.get("classes", []):
                cls_name = cls.get("name", "")
                if not cls_name:
                    logger.error("Missing class name")
                    continue

                table_name = cls.get("table")
                attributes = cls.get("attributes", [])

                # Generate abbreviation if missing
                if not cls.get("abrev"):
                    cls["abrev"] = f"{theme_name[0].upper()}{cls_name[0:3].lower()}"

                # Process attributes
                if attributes:
                    attributes_in_model = []
                    for att in attributes:
                        att_type = att.get("att_type")
                        att_name = att.get("name")
                        att_value = att.get("value")

                        pairs = None

                        # Get coded domain values
                        if att_type == "CD" and att_value:
                            pairs = self._get_coded_values(att_value)

                        # Get subtype values
                        elif att_type == "subtype" and att_value:
                            pairs = self._get_subtype_values(att_value)

                        # Get annex table values
                        elif att_type == "annex" and att_value:
                            if att_value.endswith("_CD"):
                                pairs = self._get_coded_values(att_value)
                            else:
                                pairs = self._get_table_values(att_value)

                        if pairs:
                            att["pairs"] = pairs

                        if att.get("change", "") != "removed":
                            attributes_in_model.append(att_name)
                        # TODO missing attribute
                        if not att.get('change'):
                            att['change'] = ''
                        if not att.get('cardinality'):
                            att['cardinality'] = ''

                    # Check consistency with database
                    if table_name:
                        try:
                            self._check_attribute_consistency(
                                cls_name, table_name, attributes_in_model, cls["abrev"]
                            )
                        except Exception as e:
                            logger.error(f"Consistency check error for {cls_name}: {e}")

        # Process annexes
        for annex in model.get("annexes", []):
            annex_name = annex.get("name")
            annex_fname = annex.get("fname")
            annex_type = annex.get("type_")

            if annex_fname and annex_type == 'list':
                # Load from file
                pairs = self._get_table_values(annex_fname.replace(".json", ""))
            else:
                # Load from coded domain
                pairs = self._get_coded_values(annex_name)

            annex["pairs"] = pairs

        # Add translation statistics
        if translator:
            logger.info(f"Translation failures: {translator.get_failed_count()}")
            if translator.get_failed_count() > 0:
                logger.debug(f"Failed translations: {translator.get_failed_strings()}")

        return model

    def generate_markdown(self, model_file: str, lang: str, output_dir: str):
        """Generate Markdown documentation"""
        import jinja2
        from datetime import datetime

        # Process the model
        model_data = self.process_model(model_file)
        model_data["lang"] = lang
        model_data["date"] = datetime.now()

        # Find templates directory
        template_dir = Path(__file__).parent.parent / "templates"
        if not template_dir.exists():
            raise FileNotFoundError(f"Templates directory not found: {template_dir}")

        # Setup Jinja2
        loader = jinja2.FileSystemLoader(str(template_dir))
        env = jinja2.Environment(autoescape=True, loader=loader)
        # TODO: for debuging
        env = jinja2.Environment(
            autoescape=True,
            loader=loader,
            undefined=jinja2.StrictUndefined  # This is the magic line!
        )

        # Add custom filters (simplified versions from original)

        def slugify(input):
            return re.sub(r"[\W_]+", "-", input.lower())

        def remove_prefix(value, prefixes=self.prefixes):
            for prefix in prefixes:
                if value.startswith(prefix):
                    return value[len(prefix) :]
            return value

        def strip_final_dot(value):
            ori = value
            modified = value.strip().rstrip(".")
            if ori != modified:
                logger.debug(f"FOUND: {modified}")
            return modified

        # Define the custom filter function
        def format_date_locale(value, format="MMMM yyyy", locale="de_CH"):
            return babel.dates.format_date(date=value, format=format, locale=locale)

        def attribute_name(attribute):
            alias = attribute.get("alias")
            if alias:
                return alias
            return attribute.get("name")

        def highlight(input, words=self.classnames, linkify=True):
            words.sort(key=len, reverse=True)  # longer first
            pattern = "({})".format(r"\b|\b".join(words))

            p = re.compile(pattern)
            if linkify:
                output = input
                if re.search(pattern, input) is not None:
                    matches = re.finditer(p, input)

                    for i, m in enumerate(matches):
                        word = m.group(1)
                        output = output.replace(
                            f" {word} ", f" [{word}](#{slugify(word)}) "
                        )
                return output

            return p.sub(r"**\1**", input)

        # TODO translation fall back is too easy
        def translate_filter(geol_code, fallback_text, target_lang="FR"):
            translator = self._get_translator()
            return translator.translate(
                str(geol_code), fallback_text, target_lang.upper()
            )

        '''def translate_filter(geol_code):
            """Translate geological code to default language."""
            return translator.translate(geol_code, lang=lang.upper())'''

        def translate_de_filter(geol_code):
            """Translate geological code to German."""
            translator = self._get_translator()
            return translator.translate(geol_code, 'missing', lang="DE")

        def translate_fr_filter(geol_code):
            """Translate geological code to French."""
            translator = self._get_translator()
            return translator.translate(geol_code,'missing',  lang="FR")

        def translate_ui(text, **kwargs):
          # Simulate translation (you can hook into any i18n system here)
          translated = text  # Replace with actual translation logic if needed
          return translated % kwargs if kwargs else translated

        # TODO
        env.globals["_"] = translate_ui

        env.filters["slugify"] = slugify
        env.filters["highlight"] = highlight
        env.filters["tr"] = translate_filter
        # TODO
        env.filters["tr_de"] = translate_de_filter
        env.filters["tr_fr"] = translate_fr_filter
        env.filters["format_date_locale"] = format_date_locale
        env.filters["remove_prefix"] = remove_prefix
        env.filters["attribute_name"] = attribute_name
        env.filters["strip_final_dot"] = strip_final_dot

        # Ensure output directory exists
        output_path = Path(output_dir) / lang
        output_path.mkdir(parents=True, exist_ok=True)



        # Write JSON file (for debugging/reference)
        json_file = output_path / f"{Path(model_file).stem}.json"
        with open(json_file, "w", encoding="utf-8") as f:
            # Custom encoder for datetime objects
            import json
            from datetime import datetime, date

            def json_encoder(obj):
                if isinstance(obj, (datetime, date)):
                    return obj.isoformat()
                raise TypeError(f"Object {obj} is not JSON serializable")

            json.dump(model_data, f, indent=4, ensure_ascii=False, default=json_encoder)

            logger.info(f"Saving model data as JSON: {json_file}")

        try:
            # Render template
            template = env.get_template("model_markdown.j2")
            rendered_content = template.render(model_data)
        except jinja2.UndefinedError as e:
                logger.error(f"❌ Missing variable: {e}")
                logger.error("Available variables:")
                for key in model_data.keys():
                    logger.error(f"  - {key}: {type(model_data[key])}")
                raise
        except Exception as e:
                logger.error(f"❌ Template error: {e}")
                logger.error(f"Error type: {type(e)}")
                import traceback
                logger.error(traceback.format_exc())
                raise


        try:
            logger.info(rendered_content)



            # Write markdown file
            md_file = output_path / f"{Path(model_file).stem}.md"
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(rendered_content)



            # Generate metadata file
            metadata_template = (
                env.get_template("metadata.yaml.j2")
                if env.list_templates(filter_func=lambda x: x == "metadata.yaml.j2")
                else None
            )
            if metadata_template:
                metadata_content = metadata_template.render(model_data)
                metadata_file = output_path / "metadata.yaml"
                with open(metadata_file, "w", encoding="utf-8") as f:
                    f.write(metadata_content)

            logger.info(f"Generated documentation in {output_path}")
            return output_path

        except Exception as e:
          import traceback

          logger.error(f"Generation failed: {traceback.format_exc()}")



