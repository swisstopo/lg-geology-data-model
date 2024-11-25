# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import datetime
import html
import json
import logging
import os
import pathlib
import re
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path

import pandas as pd
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import DoubleQuotedScalarString as dq

from geocover.config import abreviations, tables
from geocover.utils import remove_abrev

# Constants
TRAD_CSV = "GeolCodeText_Trad_230317.csv"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_geol_codes(schema_path, subtypes_path, use_translation=False):
    data = []
    trad = None

    try:
        if sys.version_info >= (3, 9):
            from importlib import resources

            with resources.path("geocover.data", TRAD_CSV) as csv_path:
                trad = pd.read_csv(csv_path, sep=";")
        else:
            import pkg_resources as resources

            csv_path = resources.resource_filename("geocover.data", TRAD_CSV)
            trad = pd.read_csv(csv_path, sep=";")
    except Exception as e:
        logger.error(f"Failed to load translation CSV '{TRAD_CSV}': {e}")
        return pd.DataFrame()  # Return empty DataFrame if loading fails

    # Process GeolCode and German translations
    if use_translation:
        try:
            geol_codes = list(zip(trad["GeolCodeInt"], trad["DE"]))
            for key, val in geol_codes:
                data.append(("traduction", int(key), remove_abrev(val)))
        except KeyError as e:
            logger.error(f"Missing expected column in CSV '{TRAD_CSV}': {e}")
            return pd.DataFrame()

    # Load geocover schema and subtypes
    try:
        with open(schema_path, "r") as f:
            domains = json.load(f).get("domains", {})

        with open(subtypes_path, "r") as f:
            subtypes = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Failed to load schema or subtypes file: {e}")
        return pd.DataFrame()

    # Process subtypes
    for key, val in subtypes.items():
        try:
            data.append(("subtype", int(key), remove_abrev(val)))
        except ValueError as e:
            logger.warning(f"Invalid subtype key or value ({key}, {val}): {e}")

    # Process domains
    for domain_name, domain in domains.items():
        if not domain_name.startswith("GC_"):
            continue

        domain_type = domain.get("type")
        if domain_type:
            if domain_type == "Range":
                continue
            elif domain_type == "CodedValue":
                coded_values = domain.get("codedValues", {})
                for key, val in coded_values.items():
                    try:
                        data.append((domain_name, int(key), remove_abrev(val)))
                    except ValueError as e:
                        logger.warning(
                            f"Invalid coded value key or value in {domain_name} ({key}, {val}): {e}"
                        )
        else:
            # Process legacy domain structure
            for key, val in domain.items():
                try:
                    data.append((domain_name, int(key), remove_abrev(val)))
                except ValueError as e:
                    logger.warning(
                        f"Invalid legacy domain key or value in {domain_name} ({key}, {val}): {e}"
                    )

    # Create DataFrame and process duplicates
    df = pd.DataFrame(data, columns=["domain", "geolcode", "german"])
    if df.empty:
        logger.info("No data available after processing.")
        return df

    # Group by geolcode to aggregate source domains
    df["source"] = df.groupby("geolcode")["domain"].transform(
        lambda x: ",".join(sorted(set(x)))
    )
    df = df.drop(columns="domain").drop_duplicates(subset=["geolcode", "german"])

    # Sort by geolcode for consistency
    df.sort_values("geolcode", inplace=True)

    return df


if __name__ == "__main__":
    main()
