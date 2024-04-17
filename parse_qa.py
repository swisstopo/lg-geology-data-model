import xml.etree.ElementTree as ET
from io import StringIO  ## for Python 3
import json
import sys


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

    conditions = root.findall(
        ".//{urn:ProSuite.QA.QualitySpecifications-3.0}QualityCondition", namespaces
    )

    for condition in conditions:

        parameters = condition.find("./{urn:ProSuite.QA.QualitySpecifications-3.0}Parameters")


        desc = condition.find("./{urn:ProSuite.QA.QualitySpecifications-3.0}Description")


        scalars = parameters.findall("./{urn:ProSuite.QA.QualitySpecifications-3.0}Scalar")
        dataset = parameters.find("./{urn:ProSuite.QA.QualitySpecifications-3.0}Dataset")

        print(f"========={dataset.attrib['value']} ==========")
        if desc is not None:
            print(desc.text)
        scalar_values = [s.attrib['value'] for s in scalars if s.attrib['parameter'] == "constraint"]

        expressions = []
        expr = []
        for v in scalar_values:
            if  v.strip().startswith('+'):
                expr.append(v)

            else:
                if len(expr)>0:
                    expressions.append(" ".join(expr))
                    expr=[v]
                else:
                    expr=[v]

        print(scalar_values)







get_madatory('input/QA_all_240414.qa.xml')


