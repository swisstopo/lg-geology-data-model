""" Simple script to exctract layer SubType from an ESRI ArcMap or ArcGis Pro project"""

import os
import json
import arcpy
import datetime
import sys

import logging

class UnicodeHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            # Ensure that msg is a Unicode string and encode it as UTF-8
            if isinstance(msg, unicode):
                msg = msg.encode('utf-8')
            stream.write(msg + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s",level=logging.INFO)


now = datetime.datetime.now()

try:
    curdir  = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
except NameError:
    curdir = r'H:\code\lg-geology-data-model'
basedir = os.path.abspath(os.path.join(curdir, 'exports'))

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
    if df is not None:
        layers_list=  arcpy.mapping.ListLayers(mxd, "*", df)
    else:
        layers_list =  arcpy.mapping.ListLayers(mxd, "*")


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
    print(u"==== {} ====".format(lyr.name))
    if not lyr.isFeatureLayer:
        print("Not a Feature Layer")
        continue
    fc = lyr.name
    previous_connection_info = subtypes_dict["database"].get("connection")
    if lyr.supports("DATASOURCE"):
        if lyr.dataSource:
          connection_info = None
          try:
            cp = lyr.connectionProperties
            connection_info = cp.get("connection_info")
            logging.debug(connection_info)
            logging.debug(cp["dataset"])
            if previous_connection_info is not None:
                if not previous_connection_info == connection_info:
                    logging.error("Connection is different form the previous one.")
                    sys.exit(2)
          except AttributeError:
              print(u"Layer {} has no connection properties".format(lyr.name))

        try:
            desc_lu = {key: value["Name"] for (key, value) in list_subtypes(fc)}
            #print(json.dumps(desc_lu, indent=4))
            subtypes_layers[fc] = desc_lu
            subtypes_dict = merge_two_dicts(subtypes_dict, desc_lu)

            subtypes_layers["database"]["connection"] = connection_info
            subtypes_dict["database"]["connection"] = connection_info

            print(subtypes_dict)


        except Exception as e:
            print(e)
            continue
    else:
        logging.error("Do not support datasource")
logging.info(json.dumps(subtypes_layers, indent=4))

with open(os.path.join(basedir, "subtypes_pro_layer.json"), "w") as f:
    f.write(json.dumps(subtypes_layers, indent=4))

fname = os.path.join(basedir, "subtypes_dict.json")
with open(fname, "w") as f:
    f.write(json.dumps(subtypes_dict, indent=4))

print(fname)
