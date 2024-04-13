import arcpy
import json
import datetime

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


now = datetime.datetime.now()


def get_connection_info(workspace):
    desc = arcpy.Describe(r"C:data\Connection to state.sde")
    cp = desc.connectionProperties

    properties = {
        "workspace": {
            "ConnectionString": desc.connectionString,
            "WorkspaceFactoryProgID": desc.workspaceFactoryProgID,
            "WorkspaceType:": desc.workspaceType,
        },
        "connection": {
            "Server": cp.server,
            "Instance": cp.instance,
            "Database": cp.database,
            "User": cp.user,
            "Version": cp.version,
        },
    }

    return properties


def get_coded_domains(workspace=r"h:/connections/GCOVERP@osa.sde", prefix="GC_"):
    arcpy.env.workspace = workspace

    domains = arcpy.da.ListDomains(arcpy.env.workspace)

    dom_dict = {
        "date": now.strftime("%d-%m%Y"),
        "database": get_connection_info(workspace),
    }

    for d in domains:
        if d.name.startswitch(prefix):
            dom_dict[d.name] = {"type": d.domainType}
            if d.domainType == "CodedValue":
                dom_dict[d.name]["codedValues"] = d.codedValues

            elif d.domainType == "Range":
                dom_dict[d.name]["range"] = d.range

        else:
            logging.info("Not adding {d.name}")


with open(r"H:/model_reporting/coded_domains.json", "w") as f:
    f.write(json.dumps(dom_dict, indent=4))
