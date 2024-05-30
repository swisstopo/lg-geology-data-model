import arcpy
import pandas as pd
import os
import sys

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

TREE_TABLES = ['litho', 'litstrat', 'chrono', 'charcat']

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




aprx = arcpy.mp.ArcGISProject("CURRENT")
maps = aprx.listMaps()
try:
    curdir  = os.path.dirname(os.path.realpath(__file__))
except NameError:
    curdir = r'H:\code\geocover-examples\datamodel'
basedir = os.path.join(curdir, 'exports')

if not  os.path.isdir(basedir):
    os.makedirs(basedir)

fields = list(
    (
        "OBJECTID",
        "GEOL_CODE",
        "GEOL_CODE_INT",
        "GERMAN",
        "FMAT_LITSTRAT",
        "GERMAN",
        "TREE_LEVEL",
        "PARENT_REF",
    )
)

with pd.ExcelWriter(os.path.join(basedir, f"export_tables.xlsx")) as writer:
    for mp in maps:
        logging.info("--------------------------------------------------------------")
        logging.info(mp.name)
        logging.info("--------------------------------------------------------------")
        tables = mp.listTables()
        if len(tables) < 1:
            logging.error("No Table found. Exit")
            sys.exit(2)
        for table in tables:
            logging.info(table.name)

            try:
                df = arcgis_table_to_df(table.name, input_fields=fields)
                df['PARENT_REF'] = df['PARENT_REF'].fillna(0)
            except KeyError as e:
                logging.error(f"Table {table.name} has nokey: {e}")
                continue

            df.sort_values(by=['GEOL_CODE_INT', 'PARENT_REF'], inplace=True)
            #df = df.reindex(df.columns.union(fields, sort=False), axis=1, fill_value=0)

            try:
                df.to_csv(os.path.join(basedir, f"{table.name}.csv"), index=True)
                df.to_json(os.path.join(basedir, f"{table.name}.json"), index=True)
                df.to_excel(writer, sheet_name=table.name.upper())
            except PermissionError as e:
                logging.error(f"Permission error: {table}")
