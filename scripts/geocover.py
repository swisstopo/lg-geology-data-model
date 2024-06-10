#!/usr/bin/env python

import datetime
import json
import logging
import os
import sys
from collections import OrderedDict
from copy import deepcopy


import click
import pandas as pd


from utils import dump_dict_to_json

# Won't work on h:\
DEFAULT_WORKSPACE = r"D:/connections/GCOVERP@osa.sde"
curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))


@click.group(help="Command to work with TOPGIS/GeoCover ArcSDE database")
def geocover():
    pass


@geocover.command(
    "export",
    context_settings={"show_default": True},
    help="Export some ArcSDE data for use in datamodel",
)
@click.option(
    "-l",
    "--log-level",
    default="INFO",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=True
    ),
    show_default=True,
    help="Log level",
)
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False),
    help="The directory for the output",
    default=DEFAULT_OUTPUT_DIR,
)
@click.option(
    "-w",
    "--workspace",
    type=str,
    help="Workspace (SDE string or GDB)",
    default=DEFAULT_WORKSPACE,
)
def export(output_dir, workspace, log_level):
    import arcpy

    from encoder import ExtendedEncoder
    from schema import GeocoverSchema

    now = datetime.datetime.now()

    arcpy.env.workspace = workspace

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level.upper())
    logger.addHandler(logging.StreamHandler(sys.stdout))

    so = GeocoverSchema.instance(workspace)

    encoder = ExtendedEncoder()

    connection_info = so.connection_info
    logger.debug(f"Connection info: {connection_info}")
    base_dict = {
        "date": now.strftime("%H:%M:%S-%d-%m-%Y"),
        "database": connection_info,
    }

    # Export coded domains
    coded_domains_dict = deepcopy(base_dict)

    coded_domains_dict.update(so.coded_domains)

    logger.info("Writting to 'coded_domains.json'...")
    dump_dict_to_json(
        encoder.to_serializable_dict(so.coded_domains),
        os.path.join(output_dir, "coded_domains.json"),
    )

    # Export subtypes
    subtypes_dict = deepcopy(base_dict)

    subtypes_dict.update(so.subtypes)

    dump_dict_to_json(
        encoder.to_serializable_dict(subtypes_dict),
        os.path.join(output_dir, "subtypes_dict.json"),
    )

    logger.info("###### RELATIONSHIPS #########")

    logger.info(encoder.to_serializable_dict(so.relationships))

    # Export tables
    logger.info("###### TABLES #########")
    tables_dict = deepcopy(base_dict)

    tables_dict.update(so.tree_tables)

    dump_dict_to_json(
        encoder.to_serializable_dict(tables_dict),
        os.path.join(output_dir, "tables.json"),
    )
    with pd.ExcelWriter(os.path.join(output_dir, f"export_tables.xlsx")) as writer:
        for table_name, df in so.tree_tables.items():
            logger.info(table_name)

            prefix, short_name = table_name.split(".")
            short_name = short_name.replace("GC_", "").capitalize()

            if set(["PARENT_REf", "GEOL_CODE_INT"]).issubset(df.columns):
                try:
                    df["PARENT_REF"] = df["PARENT_REF"].fillna(0)
                    df.sort_values(by=["GEOL_CODE_INT", "PARENT_REF"], inplace=True)
                except KeyError as e:
                    logger.error(f"Table {table_name} has nokey: {e}")
                    continue

            logger.info(
                f"Exporting to {short_name}.csv, {short_name}.json and 'export_tables.xlsx' (sheet={short_name.upper()}"
            )
            try:
                df.to_csv(os.path.join(output_dir, f"{short_name}.csv"), index=True)
                df.to_json(os.path.join(output_dir, f"{short_name}.json"), index=True)
                df.to_excel(writer, sheet_name=short_name.upper())
            except PermissionError as e:
                logger.error(
                    f"Permission error: 'export_tables.xlsx' is probably already opened"
                )


@geocover.command(
    "schema", context_settings={"show_default": True}, help="Dumps ArcSDE schema"
)
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False),
    help="The directory for the output",
    default=DEFAULT_OUTPUT_DIR,
)
@click.option(
    "-w",
    "--workspace",
    type=str,
    help="Workspace (SDE string or GDB)",
    default=DEFAULT_WORKSPACE,
)
@click.option(
    "-l",
    "--log-level",
    default="INFO",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=True
    ),
    show_default=True,
    help="Log level",
)
def schema(output_dir, workspace, log_level):
    import arcpy
    from encoder import ExtendedEncoder
    from schema import GeocoverSchema

    arcpy.env.workspace = workspace

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level.upper())
    logger.addHandler(logging.StreamHandler(sys.stdout))

    so = GeocoverSchema.instance(workspace)

    encoder = ExtendedEncoder()

    connection_info = so.connection_info

    schema_dict = OrderedDict(
        {
            "datetime": datetime.datetime.now(),
            "relationships": so.relationships,
            "tables": so.tables,
            "featclasses": so.feature_classes,
            "domains": so.coded_domains,
            "subtypes": so.subtypes,
        }
    )

    logger.info("Writting to 'geocover-schema-sde.json'...")
    dump_dict_to_json(
        encoder.to_serializable_dict(schema_dict),
        os.path.join(output_dir, "geocover-schema-sde.json"),
    )


@geocover.command(
    "geolcode", context_settings={"show_default": True}, help="Dumps all geol codes"
)
@click.option(
    "-o",
    "--output-file",
    type=click.Path(exists=False, file_okay=True, writable=True),
    default="../exports/all_geolcode.xlsx",
    help="The file for the output",
)
@click.option(
    "-w",
    "--workspace",
    type=str,
    help="Workspace (SDE string or GDB)",
    default=DEFAULT_WORKSPACE,
)
@click.option(
    "-l",
    "--log-level",
    default="INFO",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=True
    ),
    show_default=True,
    help="Log level",
)
def geolcode(output_file, workspace, log_level):
    from all_geolcodes import get_geol_codes

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level.upper())
    logger.addHandler(logging.StreamHandler(sys.stdout))

    ext = os.path.basename(os.path.abspath(output_file)).split(".")[1]

    df = get_geol_codes()

    json_str = df.to_dict(orient="records")

    logger.info(f"Saving to {output_file}")
    if ext == "json":
        df.to_json(
            path_or_buf=output_file,
            orient="records",
            force_ascii=False,
            indent=4,
            mode="w",
        )

    if ext == "xlsx":
        df.to_excel(output_file)


if __name__ == "__main__":
    geocover()
