import click
import os
import sys
import datetime
import json

import logging

from schema import GeocoverSchema
from utils import dump_dict_to_json

DEFAULT_WORKSPACE = r"D:/connections/GCOVERP@osa.sde"

curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))



"""
connection=D:\connections\GCOVERP@osa.sde, datasets=['TOPGIS_GC.GC_ROCK_BODIES', 'TOPGIS_GC.GC_ROCK_BODIES_I', 'GRATICULES_MANAGER.GRATICULES', 'TOPGIS_GC.GC_ERRORS'], feat classes=['TOPGIS_GC.GC_REVISIONSEBENE', 'TOPGIS_GC.GC_CONFLICT_POLYGON']

connection=D:\connections\GCOVERP@osa.sde\TOPGIS_GC.GC_ROCK_BODIES, datasets=[], feat classes=['TOPGIS_GC.GC_EXPLOIT_GEOMAT_PLG', 'TOPGIS_GC.GC_LINEAR_OBJECTS', 'TOPGIS_GC.GC_POINT_OBJECTS', 'TOPGIS_GC.GC_FOSSILS', 'TOPGIS_GC.GC_UNCO_DESPOSIT', 'TOPGIS_GC.GC_BEDROCK', 'TOPGIS_GC.GC_SURFACES', 'TOPGIS_GC.GC_MAPSHEET', 'TOPGIS_GC.GC_EXPLOIT_GEOMAT_PT']

connection=D:\connections\GCOVERP@osa.sde\TOPGIS_GC.GC_ROCK_BODIES_I, datasets=[], feat classes=['TOPGIS_GC.GC_UNCO_DESPOSIT_I', 'TOPGIS_GC.GC_BEDROCK_I', 'TOPGIS_GC.GC_FOSSILS_I', 'TOPGIS_GC.GC_LINEAR_OBJECTS_I', 'TOPGIS_GC.GC_POINT_OBJECTS_I', 'TOPGIS_GC.GC_EXPLOIT_GEOMAT_PT_I', 'TOPGIS_GC.GC_EXPLOIT_GEOMAT_PLG_I', 'TOPGIS_GC.GC_SURFACES_I', 'TOPGIS_GC.GC_MAPSHEET_I']

connection=D:\connections\GCOVERP@osa.sde\GRATICULES_MANAGER.GRATICULES, datasets=[], feat classes=[]

connection=D:\connections\GCOVERP@osa.sde\TOPGIS_GC.GC_ERRORS, datasets=[], feat classes=['TOPGIS_GC.GC_ERRORS_POLYGON', 'TOPGIS_GC.GC_ERRORS_MULTIPOINT', 'TOPGIS_GC.GC_ERRORS_LINE']
"""



@click.group()
def geocover():
    pass


@click.option(
    "-l",
    "--log-level",
    default="INFO",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=True
    ),
    show_default=True,
    help="Log level",
)
@geocover.command("export", context_settings={"show_default": True})
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
def export(output_dir, workspace, log_level):
    from encoder import ExtendedEncoder
    import arcpy

    now = datetime.datetime.now()

    arcpy.env.workspace = workspace

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level.upper())
    logger.addHandler(logging.StreamHandler(sys.stdout))

    so = GeocoverSchema.instance(workspace)

    print(so.tables)

    encoder = ExtendedEncoder()


    connection_info = so.connection_info
    logger.info(f"Connection info: {connection_info}")
    coded_domains_dict = {
        "date": now.strftime("%H:%M:%S-%d-%m-%Y"),
        "database": connection_info,
    }

    coded_domains_dict.update(so.coded_domains)

    logging.info("Writting to 'coded_domains.json'...")
    dump_dict_to_json(
        encoder.to_serializable_dict(so.coded_domains),
        os.path.join(output_dir, "coded_domains.json"),
    )


@geocover.command("schema")
def schema():
    print("schema")


if __name__ == "__main__":
    geocover()
