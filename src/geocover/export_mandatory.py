import glob
import os
import xml.etree.ElementTree as ET
import json
import re
import click

import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)

xml_dir = r"\\v0t0020a.adr.admin.ch\topgisprod\10_Production_GC\CorporateEditor\AE"

try:
    curdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
except NameError:
    curdir = r"H:\code\lg-geology-data-model"
DEFAULT_OUTPUT_DIR = os.path.abspath(os.path.join(curdir, "exports"))


PREFIXES = [
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

    p = re.compile("|".join(map(re.escape, PREFIXES)))

    for sub in subs:
        field = p.sub("", sub.attrib["field"])

        mandatory[field] = bool(sub.attrib.get("required", False))

    return mandatory


@click.command(context_settings={"show_default": True})
@click.option(
    "-o",
    "--output-dir",
    type=click.Path(exists=True, file_okay=False),
    help="The directory for the output",
    default=DEFAULT_OUTPUT_DIR,
)
def main(output_dir):
    xml_files = get_xml_files()

    madatory = {}

    for fname in xml_files:
        basename = os.path.basename(fname).replace(".ae.xml", "")
        logging.info(f"==={basename}===")
        madatory[basename] = get_madatory(fname)

    output_filename = os.path.join(output_dir, "mandatory.json")

    logging.info(f"Writing to: {output_filename}")

    with open(output_filename, "w") as f:
        f.write(json.dumps(madatory, indent=4))


if __name__ == "__main__":
    main()
