#!/usr/bin/env python3

import os
import json
import pygraphviz as pgv

from sql2puml import SQL2PUML

FONTNAME = "DejaVu Sans,Nimbus Sans"


def removeprefix(prefix, lst):
    return [i.replace(prefix, "") for i in lst]


def clean(s):
    if isinstance(s, list):
        cleaned = list(map(lambda x: x.replace("TOPGIS_GC.", ""), s))
        if len(cleaned) == 1:
            return cleaned[0]
        else:
            return cleaned
    else:
        return s.replace("TOPGIS_GC.", "")


IGNORE_FIELDS = [
    "OPERATOR",
    "DATEOFCREATION",
    "DATEOFCHANGE",
    "CREATION_YEAR",
    "CREATION_MONTH",
    "REVISION_YEAR",
    "REVISION_MONTH",
    "REASONFORCHANGE",
    "OBJECTORIGIN",
    "OBJECTORIGIN_YEAR",
    "OBJECTORIGIN_MONTH",
    "KIND",
    "RC_ID",
    "WU_ID",
    "RC_ID_CREATION",
    "WU_ID_CREATION",
    "REVISION_QUALITY",
    "ORIGINAL_ORIGIN",
    "INTEGRATION_OBJECT_UUID",
    "SHAPE.AREA",
    "SHAPE.LEN",
    "MORE_INFO",
]


IGNORE_OBJECTS = clean(
    [
        "DELIVERY_MANAGER.TOPDV_RELEASE_CHANGES",
        "TOPGIS_GC.GC_CONFLICT_ROW",
        "GC_ERRORS_ROW",
        "DELIVERY_MANAGER.TOPDV_RELEASE_INFO",
        "TOPGIS_GC.GC_VERSION",
        "TOPGIS_GC.GC_ERRORS_MULTIPOINT",
        "TOPGIS_GC.GC_ERRORS_POLYGON",
        "TOPGIS_GC.GC_REVISIONSEBENE",
        "TOPGIS_GC.GC_CONFLICT_POLYGON",
        "TOPGIS_GC.GC_FOSSILS",
        "TOPGIS_GC.GC_ERRORS_LINE",
        "GC_VERSION",
        "GC_MAPSHEET",
        "GC_CONFLICT_ROW",
    ]
)


class Column:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_


class ColumnFK(Column):
    def __init__(self, name, type_, reference):
        super().__init__(name, type_)
        self.reference = reference


class Table:
    def __init__(self, name):
        self.name = name
        self.columns = []

    def get_column(self, name, erase=True):
        for i, c in enumerate(self.columns):
            if c.name == name:
                if erase:
                    return self.columns.pop(i)
                else:
                    return c
        return None


class FeatureClass(Table):
    def __init__(self, name, geo):
        super().__init__(name)
        self.geometry = geo


input_file = "../data/geocover-schema-sde.json"

basename = os.path.splitext(os.path.basename(input_file))[0]


output_file = basename + ".png"
dotfile = basename + ".dot"


with open(input_file, "r") as f:
    c = f.read()


s = json.loads(c)

tables = {}

S = SQL2PUML()
G = pgv.AGraph(strict=False, directed=False)

G.graph_attr["label"] = "GCOVERP Schema (SDE)"
G.graph_attr["fontname"] = FONTNAME
G.graph_attr["fontsize"] = 50
G.graph_attr["labelloc"] = "t"


G.node_attr["shape"] = "box"
G.node_attr["style"] = "filled"
G.node_attr["color"] = "lightblue"
G.node_attr["fontname"] = FONTNAME

G.edge_attr["len"] = 2.00
G.edge_attr["fontname"] = FONTNAME


for t in s["tables"].keys():
    if t.endswith("_I") or clean(t) in IGNORE_OBJECTS:
        continue
    G.add_node(clean(t))  # adds node 'a'
    S.add_table(clean(t))

    fields = s["tables"][t].get("fields", [])

    tt = Table(clean(t))
    for field in fields:
        name = field.get("name")
        if name in IGNORE_FIELDS:
            continue
        typ = field.get("type")
        S.add_column(name, typ)
        tt.columns.append(Column(name, typ))
    tables[clean(t)] = tt


G.node_attr["color"] = "lightcoral"
for f in s["featclasses"].keys():
    fields = s["featclasses"][f]["fields"]
    f = clean(f)
    if f.endswith("_I") or clean(f) in IGNORE_OBJECTS:
        continue
    G.add_node(clean(f))  # adds node 'a'
    S.add_table(clean(f))
    t = FeatureClass(clean(f), "pnt")
    for field in fields:
        name = field.get("name")
        if name in IGNORE_FIELDS:
            continue
        typ = field.get("type")
        S.add_column(name, typ)
        t.columns.append(Column(name, typ))
    tables[clean(f)] = t

G.node_attr["color"] = "lightgrey"
G.node_attr["style"] = "filled"
G.node_attr["shape"] = "diamond"


relations = [r for r in s["relationships"].keys() if not r.endswith("_I")]

for i, r in enumerate(relations):
    cr = clean(r)
    rr = s["relationships"][r]
    cardinality = rr["cardinality"]

    G.add_node(rr.get("forwardPathLabel", str(i)))


for i, r in enumerate(relations):
    rr = s["relationships"][r]
    cr = clean(r)
    cardinality = rr["cardinality"]
    origin = clean(rr["origin"])
    destination = clean(rr["destination"])
    fwd_label = rr.get(
        "forwardPathLabel",
        str(i),
    )
    if cardinality.startswith("One"):
        fwd_lbl = "1"
    else:
        fwd_lbl = "n"
    if cardinality.endswith("Many"):
        rev_lbl = "m"
    else:
        rev_lbl = "1"
    print(cr, f"({cardinality}):", origin, "-->", destination)
    G.add_edge(origin, fwd_label, label=fwd_lbl)
    G.add_edge(fwd_label, destination, label=rev_lbl)

    if cardinality == "OneToMany":
        ori_table = tables.get(origin)
        dest_table = tables.get(destination)
        keys = rr.get("originClassKeys")
        pri_key = None
        fk_key = None
        for k in keys:
            role = k["role"]
            name = k["name"]
            if role == "OriginPrimary":
                pri_key = name
            else:
                fk_key = name
        if fk_key is None or pri_key is None:
            print("ERROR")
            continue

        # fk = ColumnFK(name, type_, reference

        kk = ori_table.get_column(pri_key, erase=False)
        print(f"FK: {pri_key}", [col.name for col in ori_table.columns], kk)
        if kk is not None:
            type_ = kk.type_
            col = ColumnFK(fk_key, type_, origin)
            dest_table.columns.append(col)


G.layout()  # default to neato
G.layout(prog="neato")  # use dot

G.draw(output_file)  # write previously positioned graph to PNG file
# G.draw("file.ps", prog="circo")  # use circo to position, write PS file
G.draw(basename + ".svg")
G.write(dotfile)

with open("ER-Diagram.puml", "w") as f:
    f.write(S.transform())

print(
    "Generate with: dot -Tpng -Kneato -Gsize=8.3,11.7\! -Gdpi=254 -o{} {}".format(
        output_file, dotfile
    )
)

import pprint

S = SQL2PUML()
for name, table in tables.items():
    S.add_table(name)
    # pprint.pprint(table.columns)
    for col in table.columns:
        if isinstance(col, ColumnFK):
            # print(f"{col.name} is foreign")
            S.add_column_foreign(col.name, col.type_, col.reference)
        else:
            # print(f"{col.name} is not foreign {type(col)}")
            S.add_column(col.name, col.type_)
for table_name, table in S.puml_tables.items():
    # print(table_name)
    for fk in table["foreign"].values():
        pass  # print(fk)
with open("ER-Diagram.puml", "w") as f:
    f.write(S.transform())
