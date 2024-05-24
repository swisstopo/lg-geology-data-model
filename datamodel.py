import yaml
import json
import pprint
import pandas as pd
import sys
import datetime
import re
import os

import click




from loguru import logger

logger.add("datamodel.log", backtrace=False)


with open("coded_domains.json", "r") as f:
    domains = json.load(f)

with open("subtypes.json", "r") as f:
    subtypes = json.load(f)


df = pd.read_csv("../data/GeolCodeText_Trad_230317.csv", sep=";")

po_header_tpl = '''
# SOME DESCRIPTIVE TITLE
# Copyright (C) YEAR Free Software Foundation, Inc.
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\n"
"POT-Creation-Date: 2008-02-06 16:25-0500\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
"Language-Team: LANGUAGE <LL@li.org>\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=CHARSET\n"
"Content-Transfer-Encoding: ENCODING\n"'''


def create_msg(df):
    
    print(df.columns)

    de = list(zip(df['GeolCodeInt'], df['DE']))

    fr  =list(zip(df['GeolCodeInt'], df['FR']))

    msgs = {}
    msgs['de'] = "\n".join([f'\nmsgid "{m[0]}"\nmsgstr "{m[1]}"' for m in de])
    msgs['fr'] = "\n".join( [f'\nmsgid "{m[0]}"\nmsgstr "{m[1]}"' for m in fr])
    empty_pot= "\n".join( [f'\nmsgid "{m[0]}"\nmsgstr ""' for m in fr])

    
    
    for lang in ('de', 'fr'):
        locale_dir = f'./locale/{lang}/LC_MESSAGES'
        if not os.path.isdir(locale_dir):
            os.makedirs(locale_dir)
            
        with open(os.path.join(locale_dir, 'datamodel.po'), 'w') as f:
            f.write(po_header_tpl + msgs[lang])
    with open(os.path.join('locale', 'datamodel.pot'), 'w') as f:
            f.write(po_header_tpl + empty_pot)
create_msg(df)

df = df.set_index(["GeolCodeInt"])

def translate(geol_code, lang="FR"):
   
    msg = ""
    if lang in ("DE", "FR"):
        try:
            msg = df.loc[int(geol_code)]["FR"]
        except KeyError as ke:
            logger.error(f"GeolCode not found while translating '{geol_code}': {ke}")
        except Exception as ke:
            logger.error(f"Unknown error while translating '{geol_code}': {e}")

    return msg


def get_coded_values(value):
    if value in domains.keys():
        domain = domains.get(value)
        # print(f"  {name}, {att_type} , {value}")
        if domain.get("type") == "CodedValue":
            return domain.get("codedValues")

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
            return self._model

    def to_json(self):
        model = self.model.copy()

        for theme in model["themes"]:
            for cls in theme.get("classes"):
                attributes = cls.get("attributes")
                cls['abrev'] = f"{theme['name'][0].upper()}{cls['name'][0:3].lower()}"
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
        for annex in model.get("annexes"):
            pairs = get_coded_values(annex.get("name"))
            annex["pairs"] = pairs

        return model

    def to_markdown(self):
        now = datetime.datetime.now()

        # print(json.dumps(model, indent=4))
        print(f"# Datenmodel GeoCover ({now.strftime('%x')})")
        print(f'![geocover](geocover.png "GeoCover")')

        for theme in self.model["themes"]:
            print("")
            print(f"## Thema {theme.get('name','').replace('_', ' ')}")
            for cls in theme.get("classes"):
                print(f"### Klasse {cls.get('name')}")
                desc = cls.get("description", None)
                if desc is not None:
                    print(f"_{desc}_")
                print("")
                attributes = cls.get("attributes")
                if attributes:
                    for att in attributes:
                        name = att.get("name")
                        att_type = att.get("att_type")
                        value = att.get("value")
                        desc = att.get("description", None)
                        print(f"**Attribute {name.upper()}** \n")
                        if desc is not None:
                            print(f"_{desc}_ \n")

                        pairs = None

                        if att_type in ("integer", "range", "string", "float"):
                            print(f"Type: {att_type}\n")
                        if att_type == "CD" and value is not None:
                            pairs = get_coded_values(value)
                        if att_type == "subtype" and value is not None:
                            pairs = get_subtype(value)

                        if pairs is not None:
                            print("")
                            print("|GeolCode|Deutsch|Français|")
                            print(
                                "|---------------|------------------------------|------------------------------|"
                            )
                            for k in sorted(pairs):
                                de = pairs[k]
                                try:
                                    fr = df.loc[int(k)]["FR"]
                                except Exception as e:
                                    logger.error(f"{de} is not translated")
                                    fr = ""

                                print(f"|    {k:>10}| {de}|{fr}|")
                            print("")
                        print("")

@click.command()
@click.option('--lang', prompt='Language to generate', type=click.Choice(['de', 'fr'], case_sensitive=False),
              help='Language for the document')
def datamodel(lang):
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
    # Parsing
    Locale.negotiate(['de_DE', 'en_US'], ['de_DE', 'de_AT'])
    

   
    

    yaml_file = "datamodel.yaml"
    yaml_dir = os.path.dirname(os.path.realpath(__file__))

    project_name = Path(yaml_file).stem
    model = Report(yaml_file)
    
    

    # model.to_markdown()

    classe_names = get_classes(model.model)

    data = model.to_json()

    loader = jinja2.FileSystemLoader(os.path.join(yaml_dir, 'templates'))
    env = jinja2.Environment(autoescape=True, loader=loader, extensions=["jinja2.ext.i18n"])
    
    
    # TODO: only one language
    translations = Translations.load('locale', [lang], 'datamodel')
    ui_translations = Translations.load('locale', [lang], 'app')
    
    translations.merge(ui_translations)
    data['lang'] = lang
    

    env.install_gettext_translations(translations,  newstyle=True)
    
    

    def slugify(input):
        """Custom filter"""
        return re.sub(r"[\W_]+", "-", input.lower())

    def highlight(input, words=classe_names, linkify=True):
        words.sort(key=len, reverse=True)  # longer first
        pattern = "({})".format(r"\b|\b".join(words))

        p = re.compile(pattern)
        if linkify:
            output = input
            if re.search(pattern, input) is not None:
                matches = re.finditer(p, input)

                print("---")
                print(input)
                for i, m in enumerate(matches):
                    word = m.group(1)
                    print(i, word)
                    output = output.replace(
                        f" {word} ", f" [{word}](#{slugify(word)}) "
                    )
            return output

        return p.sub(r"**\1**", input)

    env.filters["slugify"] = slugify
    env.filters["highlight"] = highlight
    env.filters["tr"] = translate
    temp = env.get_template("model_markdown.j2")
    # temp.render(data)

    with open(f"{project_name}_{lang}.json", "w") as f:
        f.write(json.dumps(data, indent=4, cls=DatetimeEncoder))

    # with open("model_markdown.j2") as f:
    #    template = Template(f.read())

    #print(temp.render(data))

    with open(f"input/{project_name}_{lang}.md", "w") as f:
        # f.write(template.render(data))
        f.write(temp.render(data))
        
    # Metadata
    meta = env.get_template("metadata.yaml.j2")
    with open(f"metadata_{lang}.yaml", "w") as f:
        # f.write(template.render(data))
        f.write(meta.render(data))
        
        
     
        
       


if __name__ == "__main__":
    datamodel()
