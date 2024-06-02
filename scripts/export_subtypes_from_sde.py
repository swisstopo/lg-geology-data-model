import os
import arcpy
import json
import logging
import click
from collections import OrderedDict


logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


"""
Subtype dictionnary

{'Default': False, 'Name': 'Aexp Grube (Lockergesteinsabbau)', 'FieldValues': {'OBJECTID': (None, None), 'UUID': (None, None), 'OPERATOR': (None, None), 'DATEOFCREATION': (None, None), 'DATEOFCHANGE': (None, None), 'CREATION_YEAR': (None, <Workspace Domain object object at 0x00000164D322F270>), 'CREATION_MONTH': (None, <Workspace Domain object object at 0x00000164D322F230>), 'REVISION_YEAR': (None, <Workspace Domain object object at 0x00000164D322F1B0>), 'REVISION_MONTH': (None, <Workspace Domain object object at 0x00000164D322F1F0>), 'REASONFORCHANGE': (None, <Workspace Domain object object at 0x00000164D322F130>), 'OBJECTORIGIN': (None, <Workspace Domain object object at 0x00000164D322F170>), 'OBJECTORIGIN_YEAR': (None, <Workspace Domain object object at 0x00000164D322F0B0>), 'OBJECTORIGIN_MONTH': (None, <Workspace Domain object object at 0x00000164D322F2B0>), 'KIND': (None, None), 'RC_ID': (None, None), 'WU_ID': (None, None), 'RC_ID_CREATION': (None, None), 'WU_ID_CREATION': (None, None), 'REVISION_QUALITY': (None, None), 'ORIGINAL_ORIGIN': (None, <Workspace Domain object object at 0x00000164D322F330>), 'INTEGRATION_OBJECT_UUID': (None, None), 'MORE_INFO': (None, None), 'SYMBOL': (None, None), 'AEXP_STATUS': (None, <Workspace Domain object object at 0x00000164D322F430>), 'AEXP_TARG_MAT': (None, <Workspace Domain object object at 0x00000164D322F370>), 'SHAPE': (None, None), 'SHAPE.AREA': (None, None), 'SHAPE.LEN': (None, None)}, 'SubtypeField': 'KIND'}
                    """

# Define the path to your .sde connection file
sde_connection = r"d:\connections\GCOVERP@osa.sde"

arcpy.env.workspace = sde_connection

# List all feature classes and tables in the geodatabase
arcpy.env.workspace = sde_connection
feature_classes = arcpy.ListFeatureClasses()
tables = arcpy.ListTables()

# Get all domains in the geodatabase
domains = {domain.name: domain for domain in arcpy.da.ListDomains(sde_connection)}


EXLCUDES = ["TOPGIS_GC.GC_REVISIONSEBENE"]

# Has to be a local drive (h:\ gives OSError!
DEFAULT_WORKSPACE = r"D:/connections/GCOVERP@osa.sde"

try:
    curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
except NameError:
    curdir = r"H:\code\lg-geology-data-model"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))


class CodedDomainEncoder(json.JSONEncoder):
    def default(self, z):
        if z.__class__.__name__ == "Workspace Domain object":
            return z.name
        else:
            return super().default(z)


def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


def get_field_type(stdict):
    field_type_dict = {}
    for stkey in list(stdict.keys()):
        if stkey == "FieldValues":
            fields = stdict[stkey]
            for field, fieldvals in list(fields.items()):
                if not fieldvals[1] is None:
                    logging.info(f"   {field}: {fieldvals[1].name} {fieldvals[0]}")
                    field_type_dict[field] = fieldvals[1].name
    return field_type_dict


def list_subtypes_walking():
    subtypes_layers_dict = {}
    subtypes_dict = {}
    walk = arcpy.da.Walk(datatype="FeatureClass")
    list_subtypes = lambda x: arcpy.da.ListSubtypes(x).items()
    for root, fds, fcs in walk:
        for fc in fcs:
            if not fc.endswith("_I") and "GC_" in fc and fc not in EXLCUDES:
                logging.info(f"===={fc}====")
                try:
                    subtypes = arcpy.da.ListSubtypes(os.path.join(root, fc))
                except OSError as e:
                    logging.error(e)
                    continue
                d = []
                desc_lu = {key: value["Name"] for (key, value) in subtypes.items()}
                subtypes_dict = merge_two_dicts(subtypes_dict, desc_lu)

                for stcode, stdict in list(subtypes.items()):
                    logging.info({stcode: stdict["Name"]})
                    logging.info(f"  Subtype Code: {stcode}")
                    logging.info(f"  Subtype Name: {stdict['Name']}")
                    logging.info(f"  Subtype Field:{stdict['SubtypeField']}")
                    logging.info(f"  Subtype Default:{stdict['Default']}")

                    d.append({stcode: stdict})

                    field_type_dict = get_field_type(stdict)

                subtypes_layers_dict[fc] = d
    return (subtypes_layers_dict, subtypes_dict)





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
    arcpy.env.workspace = workspace

    subtypes_layers_dict, subtypes_dict = list_subtypes_walking()

    sorted_subtypes_dict = OrderedDict(sorted(subtypes_dict.items()))

    with open(os.path.join(output_dir, "subtypes_layers_dict.json"), "w") as f:
        f.write(json.dumps(subtypes_layers_dict, indent=4, cls=CodedDomainEncoder))

    with open(
        os.path.join(output_dir, "subtypes_dict.json"), "w", encoding="utf8"
    ) as json_file:
        json.dump(
            sorted_subtypes_dict,
            json_file,
            indent=4,
            ensure_ascii=False,
            cls=CodedDomainEncoder,
        )


if __name__ == "__main__":
    main()
