#!/usr/bin/env python3
import yaml
import json
import pprint
import pandas as pd
import sys
import datetime
import pytz
import re
import os
import subprocess

import click


from loguru import logger

input_dir = "exports"

output_dir = "inputs"

logger.add("datamodel.log", backtrace=False)

PACKAGE_NAME = 'geocover'


with open(os.path.join(input_dir, "coded_domains.json"), "r") as f:
    domains = json.load(f)

with open(os.path.join(input_dir, "subtypes_dict.json"), "r") as f:
    subtypes = json.load(f)


df = pd.read_csv(os.path.join(input_dir, "GeolCodeText_Trad_230317.csv"), sep=";")

def get_datetime_with_tz():
    # Define the Western Europe timezone
    timezone = pytz.timezone('Europe/Zurich')
    tz_aware_datetime = datetime.datetime.now(timezone)

    return  tz_aware_datetime.strftime("%Y-%m-%d %H:%M%z")

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



# TODO: 
create_msg(df)

df = df.set_index(["GeolCodeInt"])


def translate(geol_code, fallback, lang="FR"):
    msg = fallback
    if lang in ("DE", "FR"):
        try:
            msg = df.loc[int(geol_code)]["FR"]
            # TODO: should be done in the translation XLS à ciment, à matrice
            if msg.startswith("à "):
                msg = msg.replace("à ", "")

        except KeyError as ke:
            logger.warning(f"GeolCode not found while translating '{geol_code}': {ke}")

        except Exception as e:
            logger.warning(f"Unknown error while translating '{geol_code}': {e}")

    return msg


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

    def to_json(self):
        try:
            model = self.model.copy()
        except AttributeError:
            logger.error("Model must be a dictionary-like object with a copy() method.")
            return None

        for theme in model.get("themes", []):
            try:
                theme_name = theme.get("name", "")
                if not theme_name:
                    logger.error("Missing 'name' attribute in theme.")
                    return None

                for cls in theme.get("classes", []):
                    cls_name = cls.get("name", "")
                    if not cls_name:
                        logger.error("Missing 'name' attribute in class.")
                        return None
                    attributes = cls.get("attributes")
                    cls["abrev"] = (
                        f"{theme['name'][0].upper()}{cls['name'][0:3].lower()}"
                    )
                    if attributes:
                        for att in attributes:
                            att_type = att.get("att_type")
                            value = att.get("value")
                            pairs = None

                            if att_type == "CD" and value is not None:
                                pairs = get_coded_values(value)

                            if att_type == "subtype" and value is not None:
                                pairs = get_subtype(value)

                            if pairs is not None:
                                att["pairs"] = pairs
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
def datamodel(lang, datamodel, output):
    """
    Generate a markdown document from the DATAMODEL YAML-file.
    """
    import datetime
    import os
    import sys
    from jinja2 import Template
    from babel.support import Translations
    from babel.core import Locale
    import jinja2
    from pathlib import Path
    import re
    from babel import Locale
    import babel.dates

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

    classe_names = get_classes(model.model)
    prefixes = [p + " " for p in get_prefixes(model.model)]

    data = model.to_json()
    if data is None:
        raise RuntimeError("Model conversion to JSON failed, cannot proceed")
    now = datetime.datetime.now()

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

    env.install_gettext_translations(translations, newstyle=True)

    # Custom filters

    def slugify(input):
        """Custom filter"""
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

    env.filters["slugify"] = slugify
    env.filters["highlight"] = highlight
    env.filters["tr"] = translate
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
        # f.write(template.render(data))
        rendered = render_template_with_locale("model_markdown.j2", data, locale)
        f.write(rendered)

    # Metadata
    # meta = env.get_template("metadata.yaml.j2")
    metadata_fname = os.path.join(output_dir, lang, f"metadata.yaml")
    logger.info(f"Generating {metadata_fname}")
    with open(metadata_fname, "w", encoding="utf-8") as f:
        # f.write(template.render(data))
        rendered = render_template_with_locale("metadata.yaml.j2", data, locale)
        f.write(rendered)


if __name__ == "__main__":
    datamodel()
