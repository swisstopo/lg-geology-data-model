import yaml
import json
import pprint
import pandas as pd
import sys
import datetime
import re


from loguru import logger

logger.add("datamodel.log", backtrace=False)


with open("coded_domains.json", "r") as f:
    domains = json.load(f)

with open("subtypes.json", "r") as f:
    subtypes = json.load(f)


df = pd.read_csv("../data/GeolCodeText_Trad_230317.csv", sep=";")


df = df.set_index(["GeolCodeInt"])


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
        for annex in model.get('annexes'):
            pairs = get_coded_values(annex.get('name'))
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


if __name__ == "__main__":
    import datetime
    import os
    import sys
    from jinja2 import Template
    import jinja2
    from pathlib import Path
    import re

    yaml_file = "datamodel.yaml"
    yaml_dir = os.path.dirname(os.path.realpath(__file__))

    project_name = Path(yaml_file).stem
    model = Report(yaml_file)
    

    # model.to_markdown()

    classe_names = get_classes(model.model)

    data = model.to_json()

    loader = jinja2.FileSystemLoader(yaml_dir)
    env = jinja2.Environment(autoescape=True, loader=loader)

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
    temp = env.get_template("model_markdown.j2")
    # temp.render(data)

    with open(f"{project_name}.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    # with open("model_markdown.j2") as f:
    #    template = Template(f.read())

    print(temp.render(data))

    with open(f"{project_name}.md", "w") as f:
        # f.write(template.render(data))
        f.write(temp.render(data))
