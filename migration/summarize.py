import os
import io
import json
import click

import re
import yaml

REGEX_CD = r"domains\/([A-Z_-]*)\/codedValues\/(\d+)"

REGEX_FEATCLASS = r"featclasses\/([A-Z_-]*)\/\d+\/name"

test_str = "/domains/GC_TECTO_CD/codedValues/15309091"


INPUT_FILE = "migration/20221130-20241105.diff"


def get_changes(txt):
    matches = re.finditer(REGEX_CD, txt)
    if matches:
        for match in matches:
            return match.groups()

    return None


def get_att_changes(txt):
    matches = re.finditer(REGEX_FEATCLASS, txt)
    if matches:
        for match in matches:
            return match.groups()

    # print(txt)
    return None


res = {}

OPERATIONS = ("add", "replace", "move", "remove")


@click.command()
@click.argument("filename")
def summarize(filename):
    # with open('migration/production-diff-october-2024.txt', 'r') as f:
    with open(filename, "r") as f:
        lines = json.load(f)

        for line in lines:
            match = feat_class = None
            op = line.get("op")
            pth = line.get("path")

            match = get_att_changes(pth)

            if match and len(match) > 0:
                feat_class = match[0]
            if feat_class:
                if not res.get(feat_class):
                    res[feat_class] = {}
                    for operation in OPERATIONS:
                        res[feat_class][operation] = []
                if op:
                    value = line.get("value")
                    print(f"{op.capitalize()}: {feat_class}: {value}")
                    res[domain][op].append({"geolcode": code, "value": value})

            domain_code = get_changes(pth)

            if domain_code:
                domain, code = domain_code

                if not res.get(domain):
                    res[domain] = {}
                    for operation in OPERATIONS:
                        res[domain][operation] = []

                if op in ["add", "replace"]:
                    value = line.get("value")
                    print(f"{op.capitalize()}: {domain}: {code}={value}")
                    res[domain][op].append({"geolcode": code, "value": value})
                if op == "move":
                    from_path = line.get("from")
                    old_domain, old_code = get_changes(from_path)
                    if old_domain == domain:
                        print(f"Moved {domain} from {old_code} to {code}")
                        res[domain]["move"].append(
                            {"geolcode": old_code, "new_geolcode": code}
                        )
                if op == "remove":
                    print(f"Removed from {domain}: {code}")
                    res[domain]["remove"].append({"geolcode": code})

    # sorting
    for domain in res.keys():
        for operation in OPERATIONS:
            data = res[domain][operation]
            res[domain][operation] = sorted(data, key=lambda x: x["geolcode"])

    # print(json.dumps(res, indent=4, ensure_ascii=False))

    with io.open(f"{filename}.yaml", "w", encoding="utf8") as yaml_file:
        yaml.dump(
            res,
            yaml_file,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


if __name__ == "__main__":
    summarize()
