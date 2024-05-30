""" Simple script to exctract layer SubType from an ESRI ArcMap or ArcGis Pro project"""

import os
import json
import arcpy
import datetime
import sys

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

now = datetime.datetime.now()

try:
    curdir  = os.path.dirname(os.path.realpath(__file__))
except NameError:
    curdir = r'H:\code\geocover-examples\datamodel'
basedir = os.path.join(curdir, 'exports')

if not  os.path.isdir(basedir):
    os.makedirs(basedir)

if sys.version_info[0] > 2:
    is_py3 = True
    p = arcpy.mp.ArcGISProject("CURRENT")
    m = p.listMaps("*")[0]
    layers_list = [lyr for lyr in m.listLayers()]


else:
    is_py3 = False
    mxd = arcpy.mapping.MapDocument(r"CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
    layers_list = arcpy.mp.ListLayers(mxd, "", df)

if is_py3:
    list_subtypes = lambda x: arcpy.da.ListSubtypes(x).items()
else:
    list_subtypes = lambda x: arcpy.da.ListSubtypes(x).iteritems()


def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


subtypes_dict = {"date": now.strftime("%H:%M:%S-%d-%m-%Y"), "database": {}}

subtypes_layers = {"date": now.strftime("%H:%M:%S-%d-%m-%Y"), "database": {}}


for lyr in layers_list:
    logging.info("==== {} ====".format(lyr.name))
    if not lyr.isFeatureLayer:
        logging.info("Not a Feature Layer")
        continue
    fc = lyr.name
    previous_connection_info = subtypes_dict["database"].get("connection")
    if lyr.supports("DATASOURCE"):
        if lyr.dataSource:
            cp = lyr.connectionProperties
            connection_info = cp.get("connection_info")
            logging.debug(connection_info)
            logging.debug(cp["dataset"])
            if previous_connection_info is not None:
                if not previous_connection_info == connection_info:
                    logging.error("Connection is different form the previous one.")
                    sys.exit(2)
        try:
            desc_lu = {key: value["Name"] for (key, value) in list_subtypes(fc)}
            logging.info(json.dumps(desc_lu, indent=4))
            subtypes_layers[fc] = desc_lu
            subtypes_dict = merge_two_dicts(subtypes_dict, desc_lu)

            subtypes_layers["database"]["connection"] = connection_info
            subtypes_dict["database"]["connection"] = connection_info

            """fields  = arcpy.ListFields(fc)
    if "SUBTYPEFIELD" in fields:
        with arcpy.da.SearchCursor(fc, "SUBTYPEFIELD") as cur:
            for row in cur:
                logging.info(desc_lu[row[0]])
    else:
        logging.info("No 'subtypefiled'")
    """
        except Exception as e:
            logging.error(e)
            continue

with open(os.path.join(basedir, "subtypes_pro_layer.json"), "w") as f:
    f.write(json.dumps(subtypes_layers, indent=4))

with open(os.path.join(basedir, "subtypes_dict.json"), "w") as f:
    f.write(json.dumps(subtypes_dict, indent=4))
