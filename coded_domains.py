import arcpy
import json
import datetime

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

DEFAULT_WORKSPACE = r'h:/connections/GCOVERP@osa.sde'

now = datetime.datetime.now()


def get_connection_info(workspace=DEFAULT_WORKSPACE):
    desc = arcpy.Describe(workspace)
    cp = desc.connectionProperties

    print(dir(cp))

    properties = {
        "workspace": {
            "ConnectionString": desc.connectionString,
            "WorkspaceFactoryProgID": desc.workspaceFactoryProgID,
            "WorkspaceType:": desc.workspaceType,
        },
        "connection": {
            "Server": cp.server,
            "Instance": cp.instance,
            "Version": cp.version,
        },
    }

    return properties


def get_coded_domains(workspace=DEFAULT_WORKSPACE, prefix="GC_"):
    arcpy.env.workspace = workspace

    domains = arcpy.da.ListDomains(arcpy.env.workspace)

    dom_dict = {
        "date": now.strftime("%H:%M:%S-%d-%m-%Y"),
        "database": get_connection_info(workspace),
    }

    for d in domains:
        if d.name.startswith(prefix):
            dom_dict[d.name] = {"type": d.domainType}
            if d.domainType == "CodedValue":
                dom_dict[d.name]["codedValues"] = d.codedValues

            elif d.domainType == "Range":
                dom_dict[d.name]["range"] = d.range

        else:
            logging.info(f"Not adding {d.name}")
    return dom_dict


def main():
    dom_dict = get_coded_domains()
    print(dom_dict)

    with open(r"H:/model_reporting/coded_domains.json", "w") as f:
        f.write(json.dumps(dom_dict, indent=4))


if __name__ == '__main__':
    main()