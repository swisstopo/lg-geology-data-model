#!/usr/bin/env python3
import datetime
import json
import os
import pprint
import re
import subprocess
import sys
import threading

import click
import pandas as pd
import pytz
import yaml
from jsonschema import Draft7Validator, ValidationError
from jsonschema import validate as jsonschema_validate
from loguru import logger

input_dir = "exports"

output_dir = "inputs"

LOG_FILENAME = "datamodel.log"

logger.remove()
logger.add(sys.stderr, level="INFO")

if os.path.isfile(LOG_FILENAME):
    os.remove(LOG_FILENAME)
logger.add(LOG_FILENAME, backtrace=False, level="DEBUG")

PACKAGE_NAME = "geocover"


ATTRIBUTES_TO_IGNORE = [
    "PRINTED" "OBJECTORIGIN",
    "REASONFORCHANGE",
    "ORIGINAL_ORIGIN",
    "OBJECTORIGIN_YEAR",
    "OBJECTORIGIN_MONTH",
    "CREATION_YEAR",
    "CREATION_MONTH",
    "REVISION_YEAR",
    "REVISION_MONTH",
    "DATEOFCREATION",
    "DATEOFCHANGE",
    "OPERATOR",
    "UUID",
    "SHAPE",
    "RC_ID_CREATION",
    "REVISION_QUALITY",
    "SHAPE.LEN",
    "SHAPE.AREA",
    "RC_ID",
    "WU_ID",
    "WU_ID_CREATION",
]


with open(os.path.join(input_dir, "coded_domains.json"), "r") as f:
    domains = json.load(f)

with open(os.path.join(input_dir, "subtypes_dict.json"), "r") as f:
    subtypes = json.load(f)

with open(os.path.join(input_dir, "geocover-schema-sde.json"), "r") as f:
    sde_schema = json.load(f)
    featclasses_dict = sde_schema.get("featclasses")
    tables_ = sde_schema.get("tables")

    tables_dict = featclasses_dict | tables_

df = pd.read_csv(os.path.join(input_dir, "GeolCodeText_Trad_230317.csv"), sep=";")


def get_datetime_with_tz():
    # Define the Western Europe timezone
    timezone = pytz.timezone("Europe/Zurich")
    tz_aware_datetime = datetime.datetime.now(timezone)

    return tz_aware_datetime.strftime("%Y-%m-%d %H:%M%z")


datetime_with_tz = get_datetime_with_tz()

po_header_tpl = f'''# Swiss Geology Datamodel
# Copyright (C) 2024 Free Software Foundation, Inc.
# This file is distributed under the same license as the {PACKAGE_NAME} package.
# Geocover Team <geocover@swisstopo.ch>, 2024.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: {PACKAGE_NAME}"
"POT-Creation-Date: {datetime_with_tz}"
"PO-Revision-Date: {datetime_with_tz}"
"Last-Translator: geocover <geocover@swisstopo.ch>"
"Language-Team: LANGUAGE <LL@li.org>"
"Plural-Forms: nplurals=2; plural=(n != 1);"
"MIME-Version: 1.0"
"Content-Type: text/plain; charset=utf-8"
"Content-Transfer-Encoding: 8bit"'''


def get_git_revision_short_hash() -> str:
    return (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"])
        .decode("ascii")
        .strip()
    )


def create_msg(df):
    de = list(zip(df["GeolCodeInt"], df["DE"]))

    fr = list(zip(df["GeolCodeInt"], df["FR"]))

    msgs = {}
    msgs["de"] = "\n".join([f'\nmsgid "{m[0]}"\nmsgstr "{m[1]}"' for m in de])
    msgs["fr"] = "\n".join([f'\nmsgid "{m[0]}"\nmsgstr "{m[1]}"' for m in fr])
    empty_pot = "\n".join([f'\nmsgid "{m[0]}"\nmsgstr ""' for m in fr])

    for lang in ("de", "fr"):
        locale_dir = f"./locale/{lang}/LC_MESSAGES"
        if not os.path.isdir(locale_dir):
            os.makedirs(locale_dir)

        with open(os.path.join(locale_dir, "datamodel.po"), "w", encoding="utf-8") as f:
            f.write(po_header_tpl + msgs[lang])
    with open(os.path.join("locale", "datamodel.pot"), "w", encoding="utf-8") as f:
        f.write(po_header_tpl + empty_pot)


# TODO: not at the right place
create_msg(df)

df = df.set_index(["GeolCodeInt"])


class Translator:
    def __init__(self):
        self.failed_translations = 0
        self.failed_strings = []
        self._lock = threading.Lock()  # Ensures thread safety

    def translate(self, geol_code, text, lang="FR"):
        translated_text, _err = self._translate(geol_code, text, lang)
        if _err:
            with self._lock:
                self.failed_translations += 1
                self.failed_strings.append(text)

        return translated_text

    def _translate(self, geol_code, fallback, lang):
        msg = fallback
        err = False
        if lang in ("DE", "FR"):
            try:
                msg = df.loc[int(geol_code)]["FR"]
                # TODO: should be done in the translation XLS à ciment, à matrice
                if msg.startswith("à "):
                    msg = msg.replace("à ", "")

            except KeyError as ke:
                err = True
                logger.debug(
                    f"GeolCode not found while translating '{geol_code}': {ke}"
                )

            except Exception as e:
                err = True
                logger.debug(f"Unknown error while translating '{geol_code}': {e}")

        return (msg, err)

    def get_failed_count(self):
        return self.failed_translations

    def get_failed_strings(self):
        return self.failed_strings


# Custom sort key
def custom_sort_key(item):
    key, _ = item
    if key in ["999997", "999998"]:
        return float("inf")  # Ensure "999997" and "999998" come last
    return int(key)


def get_coded_values(domain_name):
    if domain_name in domains.keys():
        domain = domains.get(domain_name)
        # print(f"  {name}, {att_type} , {domain_name}")
        if domain.get("type") == "CodedValue":
            coded_values = domain.get("codedValues")
            # TODO: hack
            if "999997" in coded_values.keys():
                coded_values["999997"] = "unbekannt"
            if "999998" in coded_values.keys():
                coded_values["999998"] = "nicht anwendbar"
            # Sort the list using the custom key
            return dict(sorted(coded_values.items(), key=custom_sort_key))

    return {}


def check_attribute_in_table(cls_name, table, attributes, abrev, prefixes):
    ATTRIBUTES_TO_REMOVE = [
        "INTEGRATION_OBJECT_UUID",
        "MORE_INFO",
        "OBJECTID",
        "OBJECTORIGIN",
        "SYMBOL",
        "PRINTED",
    ] + ATTRIBUTES_TO_IGNORE

    model_attributes = []
    model_attributes_tuples = []

    prefixes = list(map(str.upper, prefixes))

    if abrev in prefixes:
        prefixes.remove(abrev)

    table_name = "TOPGIS_GC." + table.upper()

    attributes_dict = tables_dict.get(table_name)

    table_attributes = [d.get("name", "").upper() for d in attributes_dict]



    logger.debug(f"All prefixes: {prefixes}")

    for attribute in attributes:
      couple = []
      if attribute not in ATTRIBUTES_TO_REMOVE:
        couple.append(attribute.upper())
        model_attributes.append(attribute.upper())
        if attribute.lower() != "kind":

            attribute_name = (abrev + "_" + attribute).upper()
            couple.append(attribute_name)
        model_attributes_tuples.append(tuple(couple))

    # Ignore som common metadata columns
    all_table_attributes = [
        col for col in table_attributes if col not in ATTRIBUTES_TO_REMOVE
    ]

    # Ignore attributes whose prefix is not abrev
    table_attributes = [
        elem for elem in all_table_attributes if not elem.startswith(tuple(prefixes))
    ]

    #missing_in_table = [elem for tup in model_attributes_tuples if not any(e in table_attributes for e in tup) for elem in tup]


    logger.info(f"Attributes in model {cls_name}: {model_attributes}")
    logger.info(f"All attributes in feature class {table}: {all_table_attributes}")
    logger.info(f"Filtered attributes in feature class {table}: {table_attributes}")




    if table_attributes:
        try:
          table_attributes_set = set(table_attributes)
          model_attributes_set = set(model_attributes)

          missing_in_model = sorted(list(table_attributes_set - model_attributes_set))
          missing_in_table = sorted(list(model_attributes_set - table_attributes_set))

          # missing_in_table = [elem for tup in model_attributes_tuples if not any(e in table_attributes for e in tup) for elem in tup]

          missing_in_table = [
             col for col in missing_in_table if col not in table_attributes
         ]

          missing_in_table = []

          for col in model_attributes:
              if col not in table_attributes and (abrev + "_" + col).upper() not in table_attributes:
                  missing_in_table.append(col)




        except Exception as e:
            logger.error(f"{e}")


        if len(missing_in_model) > 0:
            logger.warning(
                f"Class {cls_name}: elements to add to model?: {missing_in_model}"
            )
        if len(missing_in_table) > 0:
            logger.warning(
                f"Class {cls_name} [{abrev}]: elements to remove from model? (not in feature class {table}): {missing_in_table}"
            )

    return (missing_in_model, missing_in_table)


def get_table_values(name):
    try:
        file_path = os.path.join(input_dir, name)
        df = pd.read_csv(file_path)

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        df = pd.DataFrame(data)

        # Convert to dictionary with 'GEOL_CODE_INT' as key and 'GERMAN' as value
        df["GEOL_CODE_INT"] = df["GEOL_CODE_INT"].astype(str)

        geol_dict = df.set_index("GEOL_CODE_INT")["GERMAN"].to_dict()

        return geol_dict

    except FileNotFoundError:
        logger.error(f"Error: The CSV file {file_path} was not found.")
    except pd.errors.EmptyDataError:
        logger.error("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        logger.error("Error: There was a problem parsing the CSV file.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}: {geol_dict}, {df}")

    return {}


def get_subtype(value):
    res = {}

    keys = [x for x in subtypes if str(x).startswith(str(value))]

    for key in keys:
        if key in subtypes.keys():
            value = subtypes.get(key)
            res[key] = value
    return res


def get_classes(model):
    classes = []
    for theme in model["themes"]:
        for cls in theme["classes"]:
            classes.append(cls.get("name"))
    return classes


def get_prefixes(model):
    prefixes = []
    for theme in model["themes"]:
        for cls in theme["classes"]:
            prefixes.append(cls.get("abrev"))
    return prefixes


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)


class Report:
    def __init__(self, config_file):
        self.config_file = config_file
        self._model = None

    @property
    def model(self):
        if self._model:
            return self._model
        else:
            with open(self.config_file, "rt", encoding="utf8") as f:
                self._model = yaml.load(f, Loader=yaml.FullLoader)
                self._model["date"] = str(datetime.date.today())
                self._model["hash"] = get_git_revision_short_hash()
            return self._model

    @property
    def abrevs(self):
        abrevs = []
        for theme in self.model.get("themes", []):
            try:
                for cls in theme.get("classes", []):
                    cls_abrev = cls.get("abrev")
                    if cls_abrev:
                        abrevs.append(cls_abrev)
            except (KeyError, TypeError, IndexError) as e:
                logger.error(f"Error processing theme '{theme}': {e}")
                return None
        return abrevs

    def to_json(self):
        try:
            model = self.model.copy()
        except AttributeError:
            logger.error("Model must be a dictionary-like object with a copy() method.")
            return None

        logger.debug(f"All prefixes: {self.abrevs}")

        for theme in model.get("themes", []):
            try:
                theme_name = theme.get("name", "")
                if not theme_name:
                    logger.error(f"Missing 'name' attribute in theme '{theme_name}'.")
                    return None

                for cls in theme.get("classes", []):
                    cls_name = cls.get("name", "")
                    if not cls_name:
                        logger.error(f"Missing 'name' attribute in class '{cls_name}'")
                        return None
                    table_name = cls.get("table")
                    attributes = cls.get("attributes")
                    cls["abrev"] = (
                        f"{theme['name'][0].upper()}{cls['name'][0:3].lower()}"
                    )
                    if attributes:
                        attributes_in_model = []
                        for att in attributes:
                            att_type = att.get("att_type")
                            att_name = att.get("name")
                            value = att.get("value")
                            pairs = None

                            if att_type == "CD" and value is not None:
                                pairs = get_coded_values(value)

                            if att_type == "subtype" and value is not None:
                                pairs = get_subtype(value)

                            if pairs is not None:
                                att["pairs"] = pairs
                            if att.get("change", "") != "removed":
                                attributes_in_model.append(att_name)
                        try:
                          check_attribute_in_table(
                            cls_name,
                            table_name,
                            attributes_in_model,
                            cls["abrev"],
                            self.abrevs,
                         )
                        except Exception as e:
                            logger.error(f"Check error: {e}")

            except (KeyError, TypeError, IndexError) as e:
                logger.error(f"Error processing theme '{theme}': {e}")
                return None
        for annex in model.get("annexes"):
            annex_name = annex.get("name")
            annex_fname = annex.get("fname")
            if annex_fname is not None:
                pairs = get_table_values(annex_fname)

            else:
                pairs = get_coded_values(annex_name)

            annex["pairs"] = pairs

        return model


@click.group()
def datamodel():
    """Datamodel command group"""
    pass


@click.command()
@click.argument("datamodel", type=click.Path(exists=True))
def check():
    """Check the data model for consistency or errors."""
    click.echo("Checking data model...")


@click.command()
@click.argument("datamodel", type=click.Path(exists=True))
@click.option(
    "--output",
    "-o",
    type=click.Path(file_okay=True),
    default="inputs",
    help="Directory for output markdown files",
)
@click.option(
    "--format",
    "-f",
    type=click.Choice(["XLSX", "JSON"], case_sensitive=False),
    help="Directory for output markdown files",
    default="XLSX",
)
def export(datamodel, output, format):
    """Export model to various format."""

    from geocover import model

    yaml_path = datamodel

    datamodel = model.Datamodel()
    datamodel.import_from_yaml(yaml_path)
    logger.info("Export to Excel")
    # datamodel.export_to_yaml("output.yaml")
    datamodel.export_to_excel(output)


@click.command()
@click.argument("datamodel", type=click.Path(exists=True))
def validate(datamodel):
    """Validate the model against a JSON schema."""
    click.echo("Validate the data model...")
    try:
        with open(datamodel, "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
    except Exception as e:
        logger.error(f"Error while opening/parsing {datamodel}")
        sys.exit(3)

    version = yaml_data.get("version")
    if version:
        schema_file_path = os.path.join("schema", f"json-schema-{version}.json")
        try:
            with open(schema_file_path, "r", encoding="utf-8") as file:
                schema_data = json.load(file)
        except Exception as e:
            logger.error(f"Cannot load schemo {schema_file_path}")
            sys.exit(4)

    # Validate the loaded YAML data against the schema
    validator = Draft7Validator(schema_data)

    errors = sorted(validator.iter_errors(yaml_data), key=lambda e: e.path)
    if errors:
        for error in errors:
            error_path = " -> ".join(str(p) for p in error.path)
            logger.error(f"Validation error at {error_path}: {error.message}")
    else:
        logger.info(f"YAML file {datamodel} is valid.")


@click.command()
@click.argument("datamodel", type=click.Path(exists=True))
def prettify(datamodel):
    """Prettifying the datamodel."""
    click.echo("Prettifying data model...")
    import sys

    import ruamel.yaml

    def block_style(base):
        """
        This routine walks over a simple, i.e. consisting of dicts, lists and
        primitives, tree loaded from YAML. It recurses into dict values and list
        items, and sets block-style on these.
        """
        if isinstance(base, dict):
            for k in base:
                try:
                    base.fa.set_block_style()
                except AttributeError:
                    pass
                block_style(base[k])
        elif isinstance(base, list):
            for elem in base:
                try:
                    base.fa.set_block_style()
                except AttributeError:
                    pass
                block_style(elem)

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True
    try:
        with open(datamodel) as fp:
            data = yaml.load(fp)
        block_style(data)
        with open(datamodel, "w") as fp:
            yaml.dump(data, fp)
    except (FileNotFoundError, PermissionError):
        logger.error("You do not have permission to access this file.")
    except ruamel.yaml.YAMLError as e:
        logger.error(f"An error occurred while processing the YAML file: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


@click.command()
@click.option(
    "--lang",
    prompt="Language to generate",
    type=click.Choice(["de", "fr"], case_sensitive=False),
    help="Language for the document",
)
@click.option(
    "--output",
    "-o",
    type=click.Path(file_okay=False),
    default="inputs",
    help="Directory for output markdown files",
)
@click.argument("datamodel", type=click.Path(exists=True))
def generate(lang, datamodel, output):
    """
    Generate a markdown document from the DATAMODEL YAML-file.
    """
    import datetime
    import os
    import re
    import sys
    from pathlib import Path

    import babel.dates
    import jinja2
    from babel import Locale
    from babel.core import Locale
    from babel.support import Translations
    from jinja2 import Template

    click.echo("Generating data model...")

    # Parsing
    Locale.negotiate(["de_DE", "en_US"], ["de_DE", "de_AT"])

    yaml_file = os.path.abspath(datamodel)
    yaml_dir = Path(yaml_file).parent
    if os.path.isabs(output):
        output_dir = output
    else:
        output_dir = Path(yaml_dir).joinpath(output)

    if not os.path.isdir(os.path.join(output_dir, lang)):
        os.makedirs(os.path.isdir(os.path.join(output_dir, lang)))

    logger.info(f"Markdown files ouput dir: {output_dir}")

    project_name = Path(yaml_file).stem
    try:
        model = Report(yaml_file)

    except Exception as e:
        logger.error(f"Cannot read/parse datamodel: {yaml_file}")

    # Geolcode
    xlsx_file = os.path.join(yaml_dir, "exports", "comparison_results.xlsx")
    logger.info(f"comparison file: {xlsx_file}")
    added_rows = pd.read_excel(xlsx_file, sheet_name="Added Rows")
    removed_rows = pd.read_excel(xlsx_file, sheet_name="Removed Rows")
    changed_rows = pd.read_excel(xlsx_file, sheet_name="Changed Rows")
    # Convert DataFrames to dictionaries for Jinja2
    added_rows_dict = added_rows.to_dict(orient="records")
    removed_rows_dict = removed_rows.to_dict(orient="records")
    changed_rows_dict = changed_rows.to_dict(orient="records")

    classe_names = get_classes(model.model)
    prefixes = [p + " " for p in get_prefixes(model.model)]

    data = model.to_json()
    if data is None:
        raise RuntimeError("Model conversion to JSON failed, cannot proceed")
    now = datetime.datetime.now()

    data["geolcodes"] = {}
    data["geolcodes"]["added"] = added_rows_dict
    data["geolcodes"]["removed"] = removed_rows_dict
    data["geolcodes"]["changed"] = changed_rows_dict

    loader = jinja2.FileSystemLoader(os.path.join(yaml_dir, "templates"))
    env = jinja2.Environment(
        autoescape=True,
        loader=loader,
        extensions=["jinja2.ext.i18n"],
    )

    # TODO: only one language
    locale_dir = os.path.join(yaml_dir, "locale")
    logger.info(locale_dir)
    translations = Translations.load(locale_dir, [lang], "datamodel")
    ui_translations = Translations.load(locale_dir, [lang], "app")

    translations.merge(ui_translations)
    data["lang"] = lang
    data["date"] = now
    data["hash"] = get_git_revision_short_hash()
    locale = lang

    # logger.info(json.dumps(data, indent=4,  cls=DatetimeEncoder))

    env.install_gettext_translations(translations, newstyle=True)

    # Custom filters

    def slugify(input):
        return re.sub(r"[\W_]+", "-", input.lower())

    def remove_prefix(value, prefixes=prefixes):
        for prefix in prefixes:
            if value.startswith(prefix):
                return value[len(prefix) :]
        return value

    # Define the custom filter function
    def format_date_locale(value, format="MMMM yyyy", locale="de_CH"):
        return babel.dates.format_date(date=value, format=format, locale=locale)

    def highlight(input, words=classe_names, linkify=True):
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

    translator = Translator()

    env.filters["slugify"] = slugify
    env.filters["highlight"] = highlight
    env.filters["tr"] = translator.translate
    env.filters["format_date_locale"] = format_date_locale
    env.filters["remove_prefix"] = remove_prefix

    temp = env.get_template("model_markdown.j2")

    json_fname = os.path.join(output_dir, lang, f"{project_name}.json")
    logger.info(f"Generating {json_fname}")
    with open(json_fname, "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4, cls=DatetimeEncoder))

    def render_template_with_locale(template_name, data, locale):
        template = env.get_template(template_name)
        return template.render(data, locale=locale)

    markdown_fname = os.path.join(output_dir, lang, f"{project_name}.md")
    logger.info(f"Generating {markdown_fname}")
    with open(markdown_fname, "w", encoding="utf-8") as f:
        rendered = render_template_with_locale("model_markdown.j2", data, locale)
        f.write(rendered)

    # Metadata
    metadata_fname = os.path.join(output_dir, lang, f"metadata.yaml")
    logger.info(f"Generating {metadata_fname}")
    with open(metadata_fname, "w", encoding="utf-8") as f:
        # f.write(template.render(data))
        rendered = render_template_with_locale("metadata.yaml.j2", data, locale)
        f.write(rendered)

    logger.info(f"Failed translations: {translator.get_failed_count()}")
    logger.debug(f"Failed strings: {translator.get_failed_strings()}")


# Add the sub-commands to the main command group
datamodel.add_command(check)
datamodel.add_command(generate)
datamodel.add_command(prettify)
datamodel.add_command(validate)
datamodel.add_command(export)

if __name__ == "__main__":
    datamodel()
