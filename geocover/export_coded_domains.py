import arcpy
import json
import datetime
import os
import click
import pandas as pd

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

DEFAULT_WORKSPACE = r"h:/connections/GCOVERP@osa.sde"

try:
    curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
except NameError:
    curdir = r"H:\code\lg-geology-data-model"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))

now = datetime.datetime.now()


def get_connection_info(workspace=DEFAULT_WORKSPACE):
    desc = arcpy.Describe(workspace)
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
            "Version": cp.version,
        },
    }

    return properties


def get_coded_domains(workspace=DEFAULT_WORKSPACE, prefix="GC_"):
    arcpy.env.workspace = workspace

    domains = arcpy.da.ListDomains(arcpy.env.workspace)
    dom_dict = {}

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


@click.command(context_settings={"show_default": True})
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False),
    help="The directory for the output",
    default=DEFAULT_OUTPUT_DIR,
)
@click.option(
    "-w",
    "--workspace",
    type=str,
    help="Workspace (SDE string or GDB)",
    default=DEFAULT_WORKSPACE,
)
def main(output_dir, workspace):
    connection_info = get_connection_info(workspace)
    logging.info(f"Connection info: {connection_info}")
    base_dict = {
        "date": now.strftime("%H:%M:%S-%d-%m-%Y"),
        "database": connection_info,
    }
    dom_dict = get_coded_domains()

    base_dict.update(dom_dict)

    logging.info(f"Exporting to {output_dir}...")

    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    logging.info("Writting to 'coded_domains.json'...")
    with open(os.path.join(output_dir, "coded_domains.json"), "w") as f:
        f.write(json.dumps(base_dict, indent=4))

    dd = {"domain": [], "geol_code": [], "german": []}
    for k, v in dom_dict.items():
        values = v.get("codedValues") if v.get("type") == "CodedValue" else None
        if values:
            dd["domain"].extend([k] * len(values))
            dd["geol_code"].extend(values.keys())
            dd["german"].extend(values.values())

    df = pd.DataFrame.from_dict(dd)

    try:
        logging.info("Writting to Excel 'coded_domains.xlsx'...")
        df.to_excel(
            os.path.join(output_dir, "coded_domains.xlsx"), sheet_name="CODED_DOMAINS"
        )
    except (FileNotFoundError, PermissionError, ValueError) as e:
        logging.error(f"Error: cannot write to {output_dir}: {e}")

    except Exception as e:
        logging.error(f"Unknown error while writting to file: {e}")


if __name__ == "__main__":
    main()
