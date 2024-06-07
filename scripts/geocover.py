import datetime
import json
import logging
import os
import sys
from collections import OrderedDict
from copy import deepcopy

import arcpy
import click
import pandas as pd

from encoder import ExtendedEncoder
from schema import GeocoverSchema
from utils import dump_dict_to_json

DEFAULT_WORKSPACE = r"D:/connections/GCOVERP@osa.sde"
curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))


@click.group()
def geocover():
    pass


@geocover.command("export", context_settings={"show_default": True})
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

    logging.info("Writting to 'coded_domains.json'...")
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

    print("###### RELATIONSHIPS #########")
    # print(so.relationships)

    logger.info(encoder.to_serializable_dict(so.relationships))

    # Export tables
    print("###### TABLES #########")
    tables_dict = deepcopy(base_dict)

    tables_dict.update(so.tree_tables)

    dump_dict_to_json(
        encoder.to_serializable_dict(tables_dict),
        os.path.join(output_dir, "tables.json"),
    )
    with pd.ExcelWriter(os.path.join(output_dir, f"export_tables.xlsx")) as writer:
        for table_name, df in so.tables.items():
            logging.info(table_name)

            prefix, short_name = table_name.split(".")
            short_name = short_name.replace("GC_", "")

            try:
                df["PARENT_REF"] = df["PARENT_REF"].fillna(0)
            except KeyError as e:
                logging.error(f"Table {table_name} has nokey: {e}")
                continue

            df.sort_values(by=["GEOL_CODE_INT", "PARENT_REF"], inplace=True)
            # df = df.reindex(df.columns.union(fields, sort=False), axis=1, fill_value=0)

            try:
                df.to_csv(os.path.join(output_dir, f"{short_name}.csv"), index=True)
                df.to_json(os.path.join(output_dir, f"{short_name}.json"), index=True)
                df.to_excel(writer, sheet_name=short_name.upper())
            except PermissionError as e:
                logging.error(f"Permission error: {table} is probably already opened")


@geocover.command("schema", context_settings={"show_default": True})
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

    logging.info("Writting to 'schema.json'...")
    dump_dict_to_json(
        encoder.to_serializable_dict(schema_dict),
        os.path.join(output_dir, "schema.json"),
    )


if __name__ == "__main__":
    geocover()
