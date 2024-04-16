import glob
import os
import xml.etree.ElementTree as ET
from io import StringIO  ## for Python 3
import json
from pathlib import Path
import re

xml_dir = r"\\v0t0020a.adr.admin.ch\topgisprod\10_Production_GC\CorporateEditor\AE"


prefixes = [
    "AARC_",
    "AARC_",
    "ABOR_",
    "AEXP_",
    "AEXP_",
    "FMAT_",
    "GGLA_",
    "GKAR_",
    "HCON_",
    "HPAL_",
    "HSUB_",
    "HSUR_",
    "LFOS_",
    "LGEO_",
    "LPRO_",
    "LRES_",
    "LTYP_",
    "MFOL_",
    "MPLA_",
    "PCOB_",
    "PCOH_",
    "PMOD_",
    "PSLO_",
    "RBED_",
    "RUNC_",
    "TTEC_",
]


def get_xml_files():
    return glob.glob(os.path.join(xml_dir, "*.ae.xml"))


def get_madatory(fname):
    namespaces = dict([node for _, node in ET.iterparse(fname, events=["start-ns"])])

    for name, value in namespaces.items():
        # print(name, value)
        ET.register_namespace(name, value)

    mandatory = {}

    try:
        tree = ET.parse(fname)
        root = tree.getroot()
    except Exception as e:
        print(e)

    subs = root.findall(
        ".//{urn:EsriDE.ProSuite.AE.ObjectClass-1.0}FieldControl", namespaces
    )

    p = re.compile("|".join(map(re.escape, prefixes)))

    for sub in subs:
        field = p.sub("", sub.attrib["field"])

        mandatory[field] = bool(sub.attrib.get("required", False))

    return mandatory


xml_files = get_xml_files()

madatory = {}

for fname in xml_files:
    basename = os.path.basename(fname).replace(".ae.xml", "")
    print(f"==={basename}===")
    madatory[basename] = get_madatory(fname)

with open("mandatory.json", "w") as f:
    f.write(json.dumps(madatory, indent=4))