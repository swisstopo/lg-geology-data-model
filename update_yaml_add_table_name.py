# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import os
import sys

import re
import unicodedata
import datetime
import json
import html

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
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def main():
    yaml = YAML()

    yaml.default_flow_style = False
    yaml.indent(sequence=4, offset=2)
    yaml.representer.add_representer(str, str_representer)

    with open("datamodel.yaml", "r") as f:
        data = yaml.load(f)

    for theme in data.get("themes"):
        theme_name = theme.get("name")
        for cls in theme.get("classes"):
            cls_name = cls.get("name")

            if cls_name.endswith('_L'):
                table = 'GC_LINEAR_OBJECTS'

            if cls_name.endswith('_PT'):
                if 'Fossil' in cls_name:
                    table = 'GC_FOSSILS'
                else:
                    table = 'GC_POINT_OBJECTS'
            if cls_name.endswith('_PLG'):
                if 'Bedrock' in cls_name:
                    table = 'GC_BEDROCK'
                elif 'Unco' in cls_name:
                    table = 'GC_UNCO_DESPOSIT'
                else:
                    table = 'GC_SURFACES'

            cls.insert(2, "table", table, comment="TODO: to check")

    yaml.dump(data, sys.stdout)
    from pprint import pprint

    # pprint(data)
    new_path = pathlib.Path("updated_with_table_name.yaml")

    with open(new_path, "wb") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    main()