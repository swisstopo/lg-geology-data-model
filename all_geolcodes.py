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

    data = []

    trad = pd.read_csv("../data/GeolCodeText_Trad_230317.csv", sep=";")
    print(trad.columns)

    de = list(zip(trad["GeolCodeInt"], trad["DE"]))

    with open("../data/geocover-schema-sde.json", "r") as f:
        domains = json.load(f).get("domains")

    with open("subtypes_dict.json", "r") as f:
        subtypes = json.load(f)

    for key, val in de:
        data.append(("traduction", int(key), val))

    for key, val in subtypes.items():
        data.append(("subtype", int(key), val))

    for domain_name in domains.keys():
        domain = domains.get(domain_name)
        if not domain_name.startswith("GC_"):
            continue

        for key in domain.keys():
            val = domain.get(key)

            data.append((domain_name, int(key), val))

    df = pd.DataFrame(data, columns=["domain", "geolcode", "german"])
    df["source"] = ""
    df["source"] = df.groupby(["geolcode"])["domain"].transform(lambda x: ",".join(x))
    df = df.drop("domain", axis="columns")
    df = df[["geolcode", "german", "source"]].drop_duplicates()

    df.sort_values("geolcode", inplace=True)

    print(df)
    df.to_excel("input/all_geolcode.xlsx")


if __name__ == "__main__":
    main()
