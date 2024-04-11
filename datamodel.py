import yaml
import json
import pprint
import pandas as pd
import sys
import datetime


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
        if domain.get("att_type") == "CodedValue":
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
    model = Report("datamodel.yaml")

    # model.to_markdown()

    data = model.to_json()

    with open("toto.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    from jinja2 import Template

    with open("model_markdown.j2") as f:
        template = Template(f.read())

        print(template.render(data))
