# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import datetime
import html
import json
import os
import pathlib
import re
import sys
import unicodedata
from collections import OrderedDict

import pandas as pd
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dq

from utils import remove_abrev

from config import abreviations, tables


def get_geol_codes():
    data = []

    trad = pd.read_csv("../exports/GeolCodeText_Trad_230317.csv", sep=";")

    de = list(zip(trad["GeolCodeInt"], trad["DE"]))

    with open("../exports/geocover-schema-sde.json", "r") as f:
        domains = json.load(f).get("domains")

    with open("../exports/subtypes_dict.json", "r") as f:
        subtypes = json.load(f)

    for key, val in de:
        # Remove Abrev prefix from string

        data.append(("traduction", int(key), remove_abrev(val)))

    for key, val in subtypes.items():
        try:
            data.append(("subtype", int(key), remove_abrev(val)))
        except ValueError as e:
            print(key, val)

    for domain_name in domains.keys():
        domain = domains.get(domain_name)
        if not domain_name.startswith("GC_"):
            continue

        for key in domain.keys():
            val = domain.get(key)

            data.append((domain_name, int(key), remove_abrev(val)))

    df = pd.DataFrame(data, columns=["domain", "geolcode", "german"])
    df["source"] = ""
    df["source"] = df.groupby(["geolcode"])["domain"].transform(lambda x: ",".join(x))
    df = df.drop("domain", axis="columns")
    df = df[["geolcode", "german", "source"]].drop_duplicates()

    df.sort_values("geolcode", inplace=True)

    return df


if __name__ == "__main__":
    main()
