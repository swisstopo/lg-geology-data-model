import arcpy
import pandas as pd
import os
import sys
import click
import datetime

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TREE_TABLES = ["GC_LITHO", "GC_LITSTRAT", "GC_CHRONO", "GC_TECTO"]

TABLES = ["GC_CHARCAT", "GC_ADMIXTURE", "GC_COMPOSIT"]

ALL_TABLES = TABLES + TREE_TABLES

DEFAULT_WORKSPACE = r"h:/connections/GCOVERP@osa.sde"

try:
    curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
except NameError:
    curdir = r"H:\code\lg-geology-data-model"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))

now = datetime.datetime.now()


def arcgis_table_to_df(in_fc, input_fields=None, query=""):
    """Function will convert an arcgis table into a pandas dataframe with an object ID index, and the selected
    input fields using an arcpy.da.SearchCursor.
    :param - in_fc - input feature class or table to convert
    :param - input_fields - fields to input to a da search cursor for retrieval
    :param - query - sql query to grab appropriate values
    :returns - pandas.DataFrame"""
    OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
    available_fields = [field.name for field in arcpy.ListFields(in_fc)]
    logging.debug(available_fields)
    logging.debug(input_fields)
    if input_fields:
        final_fields = list(set([OIDFieldName] + input_fields) & set(available_fields))
    else:
        final_fields = available_fields
    logging.debug("Intersection:", final_fields)
    data = [
        row for row in arcpy.da.SearchCursor(in_fc, final_fields, where_clause=query)
    ]
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
    return fc_dataframe


@click.command(context_settings={"show_default": True})
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
def main(output_dir, workspace):
    export_tables(output_dir, workspace)


def export_tables(output_dir, workspace):
    arcpy.env.workspace = workspace

    tables = []

    for table in arcpy.ListTables():
        logging.info(table)
        if table.endswith("_I"):
            continue
        prefix, short_name = table.split(".")
        if short_name not in ALL_TABLES:
            continue
        tables.append((table, short_name.replace("GC_", "")))

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)



    fields = list(
        (
            "OBJECTID",
            "GEOL_CODE_INT",
            "GEOL_CODE",
            "GERMAN",
            "FMAT_LITSTRAT",
            "TREE_LEVEL",
            "PARENT_REF",
        )
    )

    logging.info(f"Writting to {output_dir}")

    with pd.ExcelWriter(os.path.join(output_dir, f"export_tables.xlsx")) as writer:
        if len(tables) < 1:
            logging.error("No Table found. Exit")
            sys.exit(2)
        for table_name, short_name in tables:
            logging.info(table_name)

            sort_keys = ["GEOL_CODE_INT"]
            try:
                df = arcgis_table_to_df(table_name, input_fields=None)
                if "PARENT_REF" in df.columns:
                    df["PARENT_REF"] = df["PARENT_REF"].fillna(0)
                    sort_keys = ["GEOL_CODE_INT", "PARENT_REF"]
                    common_columns = set(df.columns).intersection(sort_keys)
            except KeyError as e:
                logging.error(f"Table {table_name} has nokey: {e}")
                continue
            logging.info(f"Sort keys: {common_columns}")
            df.sort_values(by=common_columns, inplace=True)
            # df = df.reindex(df.columns.union(fields, sort=False), axis=1, fill_value=0)
            # Reorder the columns (why is it no always the same?)
            # Check for missing columns
            missing_fields = [col for col in fields if col not in df.columns]

            if missing_fields:
                logging.error(f"The following columns {missing_fields} are missing from {table_name} ")

            # Reorder columns if all required columns are present
            present_columns = [col for col in fields if col in df.columns]

            df = df[present_columns]

            logging.info(f"Table: {table_name}, {df.columns}")

            try:
                df.to_csv(os.path.join(output_dir, f"{short_name}.csv"), index=True)
                df.to_json(os.path.join(output_dir, f"{short_name}.json"), index=True)
                df.to_excel(writer, sheet_name=short_name.upper())
            except PermissionError as e:
                logging.error(f"Permission error: {table} is probably already opened")


if __name__ == "__main__":
    main()
