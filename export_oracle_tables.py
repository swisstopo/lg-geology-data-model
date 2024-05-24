import sys
import arcpy

import pandas as pd

sql = """select col.column_id,
       col.owner as schema_name,
       col.table_name,
       col.column_name,
       col.data_type,
       col.data_length,
       col.data_precision,
       col.data_scale,
       col.nullable
from sys.all_tab_columns col
inner join sys.all_tables t on col.owner ='TOPGIS_GC'
and col.table_name = t.table_name
where col.table_name like '%GC_%' 
order by col.owner, col.table_name, col.column_id"""

data = []
df = None

try:
    curdir  = os.path.dirname(os.path.realpath(__file__))
except NameError:
    curdir = r'H:\code\geocover-examples\datamodel'
basedir = os.path.join(curdir, 'exports')

if not  os.path.isdir(basedir):
    os.makedirs(basedir)

try:
    # Database Connections/balrog.odc/vtest.COUNTIES
    # table = ["IFMSDB.DBO.%Property"]
    sde_conn = arcpy.ArcSDESQLExecute(r"h:\connections\GCOVERP@osa.sde")

    # Pass the SQL statement to the database.
    sde_return = sde_conn.execute(sql)
    print(sde_return)
    if isinstance(sde_return, list):
        print("Number of rows returned by query: {0} rows".format(len(sde_return)))
        for row in sde_return:
            print(row)
            data.append(row)
        print("+++++++++++++++++++++++++++++++++++++++++++++\n")

        df = pd.DataFrame(
            data,
            columns=[
                "Id",
                "Owner",
                "Table_name",
                "Col_name",
                "Data_type",
                "Data_length",
                "Data_precision",
                "Data_scale",
                "Nullable",
            ],
        )

        print(df)
        df.to_csv(os.path.join(basedir, "oracle.csv"), index=False)

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys

    tb = sys.exc_info()[2]
    print("Line %i" % tb.tb_lineno)
    print(e)
