import arcpy
import json

arcpy.env.workspace = r"h:/connections/GCOVERP@osa.sde"

doms = arcpy.da.ListDomains(arcpy.env.workspace)

dom_dict = {}

for d in doms:
    dom_dict[d.name] = {
        'type': d.domainType,
        'codedValues': d.codedValues,
        'range': d.range
    }

with open(r"H:/model_reporting/coded_domains.json", "w") as f:
    f.write(json.dumps(dom_dict, indent=4))