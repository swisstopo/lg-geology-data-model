import json
import arcpy

mxd = arcpy.mapping.MapDocument(r"CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "*")[0]


def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


subtypes_dict = {}

subtypes_layers = {}

for lyr in arcpy.mapping.ListLayers(mxd, "", df):
    print(lyr.name)
    fc = lyr.name
    try:
        desc_lu = {
            key: value["Name"] for (key, value) in arcpy.da.ListSubtypes(fc).iteritems()
        }
        print(json.dumps(desc_lu, indent=4))
        subtypes_layers[fc] = desc_lu
        subtypes_dict = merge_two_dicts(subtypes_dict, desc_lu)

        with arcpy.da.SearchCursor(fc, "SUBTYPEFIELD") as cur:
            for row in cur:
                print(desc_lu[row[0]])
    except Exception as e:
        continue

with open(r"h:/subtypes_pro_layer.json", "w") as f:
    f.write(json.dumps(subtypes_layers, indent=4))

with open(r"h:/subtypes_dict.json", "w") as f:
    f.write(json.dumps(subtypes_dict, indent=4))

    desc_lu = {
        key: value["Name"] for (key, value) in arcpy.da.ListSubtypes(fc).iteritems()
    }
    with arcpy.da.SearchCursor(fc, "SUBTYPEFIELD") as cur:
        for row in cur:
            print(desc_lu[row[0]])
