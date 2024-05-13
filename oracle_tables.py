import sys
import arcpy

import pandas as pd

sql2='''select col.column_id,
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
order by col.owner, col.table_name, col.column_id'''

data = []
df = None

try:
    # Database Connections/balrog.odc/vtest.COUNTIES
    # table = ["IFMSDB.DBO.%Property"]
    sde_conn = arcpy.ArcSDESQLExecute(
         r'h:\connections\GCOVERP@osa.sde')
    sql = "select TABLE_NAME from all_tables"  # OK
    sql = '''select TABLE_NAME from all_tables where owner='TOPGIS_GC' and table_name like '%GC_%'  order BY table_name'''
    sql = """select column_name from all_tab_columns where table_name = 'TOPGIS_GC.GC_BEDR_LITHO_GC_LITHO_BED'"""

    # Pass the SQL statement to the database.
    sde_return = sde_conn.execute(sql2)
    # table = ["C:\\Users\Administrator\\AppData\\Roaming\\ESRI\\Desktop10.2\\ArcCatalog\\Connection to DAIL13077.sde"]
    print(sde_return);

    if isinstance(sde_return, list):
        print("Number of rows returned by query: {0} rows".format(
            len(sde_return)))
        for row in sde_return:
            print(row)
            data.append(row)
        print("+++++++++++++++++++++++++++++++++++++++++++++\n")

        df = pd.DataFrame(data, columns=['Id', 'Owner', 'Table_name', 'Col_name',  'Data_type', 'Data_length', 'Data_precision', 'Data_scale', 'Nullable'])

        print(df)
        df.to_csv('output/oracle.csv', index=False)

except Exception as  e:
    # If an error occurred, print line number and error message
    import traceback, sys

    tb = sys.exc_info()[2]
    print("Line %i" % tb.tb_lineno)
    print(e)

sys.exit()

try:
    # Make data path relative
    egdb = r'h:\connections\GCOVERP@osa.sde'
    egdb_conn = arcpy.ArcSDESQLExecute(egdb)

    arcpy.env.workspace = sys.path[0]

    table_name = 'TOPGIS_GC.GC_BEDR_LITHO_GC_LITHO_BED'

    conn_path = "GCOVERP@osa.sde\\"


    columns = [c.name for c in arcpy.ListFields(conn_path + table_name) if c.name != 'SHAPE']
    sql_statement = """select {} from """.format(', '.join(columns)) + table_name

    print(sql_statement)
    print("")
    print(("{:<15}" * len(columns)).format(*columns))

    egdb_return = egdb_conn.execute(sql_statement)
    for row in egdb_return:
        print(("{:<15}" * len(row)).format(*row))


    # Get the SQL statements, separated by ; from a text string.
    sql = '''select TABLE_NAME from all_tables where owner='{0}' and table_name like '%GC_%'  order BY table_name;'''.format('TOPGIS_GC')

    sql2 = 'DESCRIBE TOPGIS_GC.GC_BEDR_LITHO_GC_LITHO_BED;'

    print("Execute SQL Statement: {0}".format(sql))


    try:
            # Pass the SQL statement to the database.
            egdb_return = egdb_conn.execute(sql)
    except Exception as err:
            print(err)
            egdb_return = False

    # If the return value is a list (a list of lists), display
    # each list as a row from the table being queried.
    if isinstance(egdb_return, list):
            print("Number of rows returned by query: {0} rows".format(
                len(egdb_return)))
            for row in egdb_return:
                print(row)
            print("+++++++++++++++++++++++++++++++++++++++++++++\n")
    else:
            # If the return value was not a list, the statement was
            # most likely a DDL statement. Check its status.
            if egdb_return == True:
                print("SQL statement: {0} ran successfully.".format(sql))
            else:
                print("SQL statement: {0} FAILED.".format(sql))
            print("+++++++++++++++++++++++++++++++++++++++++++++\n")

except Exception as err:
    print(err)