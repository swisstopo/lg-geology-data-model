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

if sys.version_info.major == 3 and sys.version_info.minor >= 9:
    # Python 3.9+ specific imports
    import importlib.resources as resources
else:
    # Imports for Python versions below 3.9
    import pkg_resources as resources


import pandas as pd
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dq

from geocover.utils import remove_abrev

from geocover.config import abreviations, tables

TRAD_CSV = "GeolCodeText_Trad_230317.csv"


def get_geol_codes(exports_dir):
    data = []

    if sys.version_info >= (3, 9):
        with resources.path("geocover.data", TRAD_CSV) as csv_path:
            trad = pd.read_csv(csv_path, sep=";")
    else:
        csv_path = resources.resource_filename("geocover.data", TRAD_CSV)

        trad = pd.read_csv(csv_path, sep=";")

    de = list(zip(trad["GeolCodeInt"], trad["DE"]))

    with open(os.path.join(exports_dir, "geocover-schema-sde.json"), "r") as f:
        domains = json.load(f).get("domains")

    with open(os.path.join(exports_dir, "subtypes_dict.json"), "r") as f:
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

        if domain.get("type") == "Range":
            continue

        if domain.get("type") == "CodedValue":
            coded_values = domain.get("codedValues", {})
            if coded_values:
                for key in coded_values.keys():
                    val = coded_values.get(key)
                    data.append((domain_name, int(key), remove_abrev(val)))
        # TODO: legacy
        else:
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
