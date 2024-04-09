import xml.etree.ElementTree as ET
from io import StringIO  ## for Python 3
import json

with open("gcover.xml", "r") as f:
    xml_str = f.read()

namespaces = dict(
    [node for _, node in ET.iterparse(StringIO(xml_str), events=["start-ns"])]
)

for name, value in namespaces.items():
    print(name, value)
    ET.register_namespace(name, value)


try:
    tree = ET.ElementTree(ET.fromstring(xml_str))
    root = tree.getroot()

except Exception as e:
    print(e)


subs = root.findall(".//Subtype", namespaces)

subtypes = {}

with open("subtype.txt", "w") as f:
    for sub in subs:
        code = sub.find("./SubtypeCode").text
        name = sub.find("./SubtypeName").text
        f.write(f"{code},{name}\n")
        subtypes[code] = name

with open("subtypes.json", "w") as f:
    f.write(json.dumps(subtypes, indent=4))
