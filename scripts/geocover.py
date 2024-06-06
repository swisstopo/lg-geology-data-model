import click
import os
import sys

from schema import GeocoverSchema

DEFAULT_WORKSPACE = r"D:/connections/GCOVERP@osa.sde"

try:
    curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
except NameError:
    curdir = r"H:\code\lg-geology-data-model"
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
def export(output_dir, workspace):
    from encoder import ExtendedEncoder
    import arcpy

    arcpy.env.workspace = workspace

    so = GeocoverSchema.instance(workspace)

    print(so.tables)

    encoder = ExtendedEncoder()
    # print(encoder.to_json(so.coded_domains, indent=4))

    # print(encoder.to_yaml(so.coded_domains))

    # print(so.datasets)
    # print(so.feature_classes)
    # print(encoder.to_yaml(so))

    # print(encoder.to_json(so.feature_classes,  indent=4))

    print("##############")

    print("datasets=", so.datasets)
    print("feature classes=", so.feature_classes.keys())

    """walk = arcpy.da.Walk(datatype="FeatureClass")
    for root, fds, fcs in walk:
        print(f"connection={root}, datasets={fds}, feat classes={fcs}\n")"""

    print("##############")
    print(encoder.to_json(so.subtypes, indent=4))


@geocover.command("schema")
def schema():
    print("schema")


if __name__ == "__main__":
    geocover()
