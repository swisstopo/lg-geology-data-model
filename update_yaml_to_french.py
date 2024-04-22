# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import os
import sys

import re
import unicodedata
import datetime
import json
import html

import pathlib

from ruamel.yaml import YAML
from bs4 import BeautifulSoup

pdfs = (
    ("it", "V2.1_IT_Modello_di_dati_geologici.txt"),
    ("en", "V2.1_EN_Data_Model_Geology.txt"),
    ("fr", "V2.1_FR_Modele_de_donnees_geologiques.txt"),
)


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super().default(obj)


def str_representer(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


def cleanup(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return html.unescape(stripped_text).strip()


def get_cls_descr(filename):
    regex = r"[\d.]+ Classe ([a-zA-Z_]+)\s([\(\),\.'’\-\w\s]*)Nom"

    dct = {}

    with open(filename, "r") as f:
        data = f.read()

    test_str = unicodedata.normalize("NFC", data)

    matches = re.findall(regex, test_str, re.MULTILINE | re.UNICODE)

    for m in matches:
        cls, descr = m
        dct[cls] = descr  # .replace('\n', '')

    return dct


def get_attr_descr(filename):
    dct = {}

    regex = r"^\d.\d.\d\s(.*)\s(.*)\s(.*)"

    regex = r"<b>(.+)<\/b>.*<br\/>\s*<i>(.*)\("
    regex = r"<b>(.+)<\/b>.*attribut(.*)<br\/>\s*<i>(.*)\("

    with open(filename, "r") as f:
        data = f.read()

    test_str = unicodedata.normalize("NFC", data)

    matches = re.findall(regex, test_str, re.MULTILINE)

    for m in matches:
        a, b, c = m
        dct[cleanup(b).lower()] = cleanup(c)

    return dct


def descr(cls, strip=False):
    desc = cls.get("description")
    if desc:
        if strip and isinstance(desc, str):
            desc = desc.strip()
        d = {}
        d["de"] = desc
        d["fr"] = None
    return d


def get_translations():
    d = {}

    for lng, fname in pdfs:
        fpath = os.path.join("doc", fname)

        msg = get_cls_descr(fpath)
        d[lng] = msg

    return d


def main():
    tr_dict = get_translations()

    yaml = YAML()

    yaml.default_flow_style = False
    yaml.indent(sequence=4, offset=2)
    yaml.representer.add_representer(str, str_representer)

    att_dict = get_attr_descr("doc/V2.1_FR_Modele_de_donnees_geologiquess.html")

    print(att_dict)

    with open("datamodel.yaml", "r") as f:
        data = yaml.load(f)

    for theme in data.get("themes"):
        for cls in theme.get("classes"):
            cls["description"] = descr(cls)
            fr = tr_dict["fr"].get(cls["name"])
            cls["description"]["fr"] = fr

            for att in cls.get("attributes"):
                att["description"] = descr(att, strip=True)
                att["description"]["fr"] = att_dict.get(att["name"], "")
                # no translation yet

    yaml.dump(data, sys.stdout)
    from pprint import pprint

    # pprint(data)
    new_path = pathlib.Path("translated.yaml")

    with open(new_path, "wb") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    main()
