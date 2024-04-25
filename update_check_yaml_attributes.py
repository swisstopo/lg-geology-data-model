# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import os
import sys

import re
import unicodedata
import datetime
import json
import html
import pandas as pd

from collections import OrderedDict


import pathlib
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dq

from ruamel.yaml import YAML
from bs4 import BeautifulSoup


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)


def str_representer(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def main():
    yaml = YAML()

    df_data = []

    yaml.default_flow_style = False
    yaml.indent(sequence=4, offset=2)
    yaml.representer.add_representer(str, str_representer)

    with open("../data/geocover-schema-sde.json", "r") as f:
        feat_classes = json.load(f).get("featclasses")

    with open("datamodel.yaml", "r") as f:
        data = yaml.load(f)

    for theme in data.get("themes"):
        theme_name = theme.get("name")
        for cls in theme.get("classes"):
            cls_name = cls.get("name")
            abrev = cls.get("abrev")
            cls_table = "TOPGIS_GC.{}".format(cls.get("table").upper())
            table_attributes = feat_classes.get(cls_table).get("fields")
            print(f"======{cls_name} ({abrev})=====")
            print(cls_table)

            available_attributes = list(map(lambda x: x.get("name"), table_attributes))
            # print(available_attributes)

            print(f"Model  DB Table")
            print("----------------")
            for att in cls.get("attributes"):
                att_name = att.get("name").upper()
                search = att_name
                all_attributs = [att for att in available_attributes if search in att]
                matching_att = [att for att in all_attributs if abrev.upper() in att]
                if len(all_attributs) == 1:
                    table_att = all_attributs[0]
                elif len(matching_att) == 1:
                    table_att = matching_att[0]
                else:
                    table_att = None

                print(f"{att_name} --> {table_att}")

                df_data.append(
                    (theme_name, cls_name, abrev, cls_table, att_name, table_att)
                )

    # yaml.dump(data, sys.stdout)
    from pprint import pprint

    df = pd.DataFrame(
        df_data,
        columns=[
            "Theme",
            "Class",
            "Abrev",
            "Table",
            "Attribute_Model",
            "Attribute_Table",
        ],
    )

    df.to_excel("input/correspondance_attributs.xlsx")

    # pprint(data)
    new_path = pathlib.Path("translated.yaml")

    # with open(new_path, "wb") as f:
    #    yaml.dump(data, f)


if __name__ == "__main__":
    main()
