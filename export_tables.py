import arcpy
import pandas as pd


def arcgis_table_to_df(in_fc, input_fields=None, query=""):
    """Function will convert an arcgis table into a pandas dataframe with an object ID index, and the selected
    input fields using an arcpy.da.SearchCursor.
    :param - in_fc - input feature class or table to convert
    :param - input_fields - fields to input to a da search cursor for retrieval
    :param - query - sql query to grab appropriate values
    :returns - pandas.DataFrame"""
    OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
    available_fields = [field.name for field in arcpy.ListFields(in_fc)]
    print(available_fields)
    print(input_fields)
    if input_fields:
        final_fields = list(set([OIDFieldName] + input_fields) & set(available_fields))
    else:
        final_fields = available_fields
    print("Intersection:", final_fields)
    data = [
        row for row in arcpy.da.SearchCursor(in_fc, final_fields, where_clause=query)
    ]
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
    return fc_dataframe


import os

aprx = arcpy.mp.ArcGISProject("CURRENT")
maps = aprx.listMaps()
basedir = r"H:\code\geocover-examples\datamodel\input"

fields = list(
    (
        "OBJECTID",
        "UUID",
        "GEOL_CODE",
        "GEOL_CODE_INT",
        "GERMAN",
        "FMAT_LITSTRAT",
        "GERMAN",
        "TREE_LEVEL",
        "PARENT_REF",
    )
)

with pd.ExcelWriter(os.path.join(basedir, f"tables.xlsx")) as writer:
    for map in maps:
        print("--------------------------------------------------------------")
        print(map.name)
        print("--------------------------------------------------------------")
        tables = map.listTables()
        for table in tables:
            print(table.name)
            df = arcgis_table_to_df(table.name, input_fields=fields)
            df.to_csv(os.path.join(basedir, f"{table.name}.csv"), index=True)
            df.to_json(os.path.join(basedir, f"{table.name}.json"), index=True)
            df.to_excel(writer, sheet_name=table.name.upper())
