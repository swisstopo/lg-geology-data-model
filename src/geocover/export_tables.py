import arcpy
import pandas as pd
import os
import sys
import click
import datetime
import json

import logging
from pathlib import Path

try:
    from config import IGNORE_FIELDS
except ModuleNotFoundError as e:
    from geocover.config import IGNORE_FIELDS

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TREE_TABLES = [
    "GC_LITHO",
    "GC_LITSTRAT",
    "GC_CHRONO",
    "GC_TECTO",
    "GC_LITSTRAT_FORMATION_BANK",
]

TABLES = [
    "GC_CHARCAT",
    "GC_ADMIXTURE",
    "GC_COMPOSIT",
    "GC_GEOL_MAPPING_UNIT",
    "GC_GEOL_MAPPING_UNIT_ATT",
    "GC_LITSTRAT_UNCO",
    "GC_CORRELATION",
]

ALL_TABLES = TABLES + TREE_TABLES


DEFAULT_WORKSPACE = r"h:/connections/GCOVERP@osa.sde"

COLUMN_TYPE_MAPPING = {
    "LITSTRAT_FORMATION_BANK": int,
    "GEOL_MAPPING_UNIT": int,
    "CHRONO_TOP": int,
    "CHRONO_BASE": int,
    "LITHO_MAIN": int,
    "LITHO_SEC": int,
    "LITHO_TER": int,
    "CORRELATION": int,
}

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

    available_fields = [field.name for field in arcpy.ListFields(in_fc)]
    OIDFieldName = [f.name for f in arcpy.ListFields(in_fc) if f.type == "OID"]
    logging.debug(f"OID field: {OIDFieldName}")
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
    if len(OIDFieldName) > 0:
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
@click.option("-a", "--all", is_flag=True, help="Export all artifacts")
@click.option("--include-i", is_flag=True, help="Include tables with _I suffix")
def main(output_dir, workspace, all, include_i):
    export_tables(output_dir, workspace, all, include_i)


def export_tables(output_dir, workspace, all, include_i):
    arcpy.env.workspace = workspace

    tables = []

    output_dir = Path(output_dir).resolve()

    logging.info(arcpy.ListTables())

    for table in arcpy.ListTables():
        logging.info(table)
        if not include_i and table.endswith("_I"):
            continue
        prefix, short_name = table.split(".")
        if not all and short_name not in ALL_TABLES:
            continue
        tables.append((table, short_name.replace("GC_", "")))

    if not os.path.isdir(output_dir):
        try:
            os.makedirs(output_dir)
        except PermissionError as e:
            logging.error(f"Cannot create {output_dir}")

    """
    GC_CHRONO =                  'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE'
    GC_LITHO =                   'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE'
    GC_LITHO_UNCO =              'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE'
     GC_LITHO_BED =              'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE'
    GC_TECTO =                   'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE'
    GC_LITSTRAT_BED =            'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE
    GC_LITSTRAT_UNCO =           'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE
    
    GC_CHARCAT =                 'TREE_LEVEL', 'PARENT_REF', 'DESCRIPTION', 'GEOLCODE
    GC_LITSTRAT_FORMATION_BANK = 'TREE_LEVEL',       'PARENT_REF', 'DESCRIPTION', 'GEOLCODE'
    
       
    GC_GEOL_MAPPING_UNIT_ATT =   'LITSTRAT_FORMATION_BANK',  'GEOL_MAPPING_UNIT', 'CHRONO_TOP', 'CHRONO_BASE', 'LITHO_MAIN',  'LITHO_SEC', 'LITHO_TER', 'CORRELATION'
       
    GC_COMPOSIT =                'DESCRIPTION', 'GEOLCODE'
    GC_SYSTEM =                  'DESCRIPTION', 'GEOLCODE'
    GC_ADMIXTURE =               'DESCRIPTION', 'GEOLCODE'
    
    
    """

    fields = list(("DESCRIPTION", "GEOLCODE"))

    logging.info(f"Writting to {output_dir}")

    if len(tables) < 1:
        logging.error("No Table found. Exiting")
        sys.exit(2)

    with pd.ExcelWriter(os.path.join(output_dir, f"export_tables.xlsx")) as writer:
        for table_name, short_name in tables:
            sort_keys = ["GEOLCODE", "PARENT_REF"]
            try:
                df = arcgis_table_to_df(table_name, input_fields=None)
                if "PARENT_REF" in df.columns and "GEOLCODE" in df.columns:
                    df["PARENT_REF"] = df["PARENT_REF"].fillna(0)

                    common_columns = set(df.columns).intersection(sort_keys)
                    logging.info(f"Sort keys: {common_columns}")
                    df.sort_values(by=common_columns, inplace=True)
            except KeyError as e:
                logging.error(
                    f"Not sorting. Table {table_name} has no sort keys {sort_keys}: {e}"
                )

            # df = df.reindex(df.columns.union(fields, sort=False), axis=1, fill_value=0)
            # Reorder the columns (why is it no always the same?)
            # Check for missing columns
            missing_fields = [col for col in fields if col not in df.columns]

            if 'GC_GEOL_MAPPING_UNIT_ATT' not in table_name and missing_fields:
                logging.warning(f"== Table {table_name} ==")
                logging.warning(f"Missing columns: {missing_fields}")
                logging.warning(f"Available columns:  {df.columns} ")

            # Reorder columns if all required columns are present
            present_columns = [col for col in fields if col in df.columns]

            # logging.info(df.head())

            filename = "_".join([w.capitalize() for w in short_name.split("_")])
            json_path = os.path.join(output_dir, f"{filename}.json")
            csv_path = os.path.join(output_dir, f"{filename}.csv")

            df.to_csv(csv_path, index=True)
            # TODO: more robust way to prepare geolcode -> description table
            if "DESCRIPTION" in present_columns and "GEOLCODE" in present_columns:
                df = df[present_columns]
                df = df[["GEOLCODE", "DESCRIPTION"]]
                df.set_index("GEOLCODE", drop=True)

                simple_dict = dict(df.values)
                logging.info(f"Writing {len(df)} features to {json_path}")

                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(simple_dict, f, ensure_ascii=False, indent=4)

            # GMU_ATT
            else:
                try:
                  orientation = "records"
                  # TODO: only for GMU_ATT
                  df = df.drop(columns=IGNORE_FIELDS, errors="ignore")

                  required_columns = set(COLUMN_TYPE_MAPPING.keys())
                  existing_columns = set(df.columns)
                  missing_columns = required_columns - existing_columns

                  if not missing_columns:
                    df = df.fillna(0).astype(COLUMN_TYPE_MAPPING)

                  df.to_json(
                    json_path,
                    indent=4,
                    index=False,
                    orient="records",
                 )

                  logging.info(f"Writing to excel: {table_name}: {df.columns} ")
                except ValueError as e:
                    logging.error(f"Error writing  {table_name} to {json_path}: {str(e)}")


            try:
                df.to_excel(writer, sheet_name=short_name.upper())
            except PermissionError as e:
                logging.error(f"Permission error: {table} is probably already opened")
    with open(os.path.join(output_dir, "README.txt"), "w") as f:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Tables exported  on {now}")

    logging.info(f"Exported {len(tables)} to {output_dir}")


if __name__ == "__main__":
    main()
