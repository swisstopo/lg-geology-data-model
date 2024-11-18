#!/usr/bin/env python3

import os
import sys
import json
import pygraphviz as pgv
import yaml

from loguru import logger

from sql2puml import SQL2PUML

FONTNAME = "DejaVu Sans,Nimbus Sans"

OUTPUT_DIR = "outputs"

logger.remove(0)
logger.add(sys.stderr, format="{time} {level} {message}", level="DEBUG")


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
        "TOPGIS_GC.GC_ERRORS_LINE",
        "GC_VERSION",
        "GC_MAPSHEET",
        "GC_CONFLICT_ROW",
    ]
)


class Column:
    def __init__(self, name, type_, primary=False):
        self.name = name
        self.type_ = type_
        self.primary = primary

    def __repr__(self):
        return f"<Column: {self.name}, {self.type_}, PK: {self.primary}>"


class ColumnFK(Column):
    def __init__(self, name, type_, reference):
        super().__init__(name, type_)
        self.reference = reference


class Table:
    def __init__(self, name, relation=False, cardinality=None):
        self.name = name
        self.columns = []
        self.relation = relation
        self.cardinality = cardinality

    def get_column(self, name, erase=True):
        for i, c in enumerate(self.columns):
            if c.name == name:
                if erase:
                    return self.columns.pop(i)
                else:
                    return c
        return None

    def __repr__(self):
        return f"<Table: {self.name}, relation: {self.relation}, columns: '{','.join([col.name for col in self.columns])}'>"


class FeatureClass(Table):
    def __init__(self, name, geo):
        super().__init__(name)
        self.geometry = geo


# TODO
input_file = "exports/geocover-schema-sde.json"

basename = os.path.splitext(os.path.basename(input_file))[0]


output_file = os.path.join(OUTPUT_DIR, basename + ".png")
dotfile = os.path.join(OUTPUT_DIR, basename + ".dot")


with open(input_file, "r") as f:
    c = f.read()


s = json.loads(c)

all_tables = {}

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
    short_name = clean(t)
    if t.endswith("_I") or short_name in IGNORE_OBJECTS:
        continue

    logger.info(f"====Table {short_name}====")
    G.add_node(short_name)  # adds node 'a'
    S.add_table(short_name)

    logger.debug(s["tables"][t])

    fields = s["tables"][t]  #.get("fields", [])

    tt = Table(short_name)
    for field in fields:
        name = field.get("name")
        if name in IGNORE_FIELDS:
            continue
        typ = (
            field.get("domain")
            if field.get("domain") is not None
            else field.get("type")
        )
        S.add_column(name, typ)
        if name.lower() == "uuid":
            primary = True
        else:
            primary = False

        tt.columns.append(Column(name, typ, primary=primary))
    all_tables[short_name] = tt

    logger.info(tt)


G.node_attr["color"] = "lightcoral"
for f in s["featclasses"].keys():
    short_name = clean(f)

    fields = s["featclasses"][f]  # ["fields"]

    if f.endswith("_I") or short_name in IGNORE_OBJECTS:
        logger.debug(short_name)
        continue
    logger.info(f"========FeatureClass {short_name}===============")
    G.add_node(short_name)  # adds node 'a'
    S.add_table(short_name)
    t = FeatureClass(short_name, "Geometry")
    for field in fields:
        name = field.get("name")
        if name in IGNORE_FIELDS:
            continue
        if name.lower() == "uuid":
            primary = True
        else:
            primary = False
        typ = (
            field.get("domain")
            if field.get("domain") is not None
            else field.get("type")
        )
        S.add_column(name, typ)
        t.columns.append(Column(name, typ, primary=primary))
    all_tables[short_name] = t

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
    short_name = clean(r)
    logger.info(f"========Relationship {short_name}===============")
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
    # print(short_name, f"({cardinality}):", origin, "-->", destination)
    G.add_edge(origin, fwd_label, label=fwd_lbl)
    G.add_edge(fwd_label, destination, label=rev_lbl)

    if cardinality == "OneToMany":
        ori_table = all_tables.get(origin)
        dest_table = all_tables.get(destination)
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
            logger.error("ERROR")
            continue

        # fk = ColumnFK(name, type_, reference

        kk = ori_table.get_column(pri_key, erase=False)
        logger.debug(f"FK: {pri_key}", [col.name for col in ori_table.columns], kk)
        if kk is not None:
            type_ = kk.type_
            col = ColumnFK(fk_key, type_, origin)
            dest_table.columns.append(col)

            all_tables[destination] = dest_table

    if cardinality == "ManyToMany":
        new_table = f"{origin}_{destination}"  # tiret not allowed
        logger.info(f"New name: '{new_table}', original: '{cr}'")
        if new_table in all_tables.keys():
            logger.info(f'Discarding Relationships "ManyToMany" {new_table}')
            continue
        ori_table = all_tables.get(origin)
        dest_table = all_tables.get(destination)
        ori_keys = rr.get("originClassKeys")
        dest_keys = rr.get("destinationClassKeys")
        pri_key = None
        fk_key = None

        def get_keys(keys):
            d = {}
            for k in keys:
                role = k["role"]
                name = k["name"]
                if "Primary" in role:
                    d["pk"] = name
                else:
                    d["fk"] = name
            return d

        keys = {}
        keys["origin"] = get_keys(ori_keys)
        keys["destination"] = get_keys(dest_keys)
        
        logger.warning(f'Relationships "ManyToMany" {ori_table.name} --> {dest_table.name}')

        t = Table(new_table, relation=True, cardinality='ManyToMany')
        # t.columns.append(Column(keys["origin"]["fk"], "int"))
        # t.columns.append(Column(keys["destination"]["fk"], "int"))
        all_tables[new_table] = t

        # fk = ColumnFK(name, type_, reference

        ori_pk = ori_table.get_column(keys["origin"]["pk"], erase=False)
        logger.debug(f"FK: {ori_pk}", [col.name for col in ori_table.columns], ori_pk)
        if ori_pk is not None:
            type_ = ori_pk.type_
            col = ColumnFK(keys["origin"]["fk"], type_, origin)
            t.columns.append(col)

        dest_pk = ori_table.get_column(keys["destination"]["pk"], erase=False)
        logger.debug(
            f"FK: {dest_pk}", [col.name for col in dest_table.columns], dest_pk
        )
        if dest_pk is not None:
            type_ = dest_pk.type_
            col = ColumnFK(keys["destination"]["fk"], type_, destination)
            t.columns.append(col)

        all_tables[destination] = t


G.layout()  # default to neato
G.layout(prog="neato")  # use dot

G.draw(output_file)  # write previously positioned graph to PNG file
# G.draw("file.ps", prog="circo")  # use circo to position, write PS file
G.draw(os.path.join(OUTPUT_DIR, basename + ".svg"))
G.write(dotfile)


logger.info(
    "Generate with: dot -Tpng -Kneato -Gsize=8.3,11.7\! -Gdpi=254 -o{} {}".format(
        output_file, dotfile
    )
)

import pprint

from ruamel.yaml import YAML
from collections import OrderedDict

db_config = {"database": "GCOVERP", "version": 1, "tables": []}

logger.info("-----------------------")

SP = SQL2PUML()
for name, table in all_tables.items():
    logger.info(f"----{name}----")
    # logger.info()

    if SP.puml_tables.get(name) is not None:
        SP.current_table = name
    else:
        SP.add_table(name)
    tt = {"name": name, "columns": []}
    # pprint.pprint(table.columns)
    for col in table.columns:
        c = {}
        if isinstance(col, ColumnFK):
            # print(f"{col.name} is foreign")
            SP.add_column_foreign(col.name, col.type_, col.reference)
            c = {
                "foreign_key": {
                    "name": col.name,
                    "type": col.type_,
                    "reference": col.reference,
                }
            }

        else:
            if col.primary is True:
                logger.debug(f"PK: {col.name}")
                SP.add_column_primary(col.name, col.type_)
            else:
                # print(f"{col.name} is not foreign {type(col)}")
                SP.add_column(col.name, col.type_)
            c = {"name": col.name, "type": col.type_, "primary_key": primary}
        tt["columns"].append(c)
    db_config["tables"].append(tt)

coded_domains = s.get("domains")
for name in coded_domains.keys():
    logger.info(f"----{name}----")
    domain_dict = coded_domains[name]
    SP.add_enum(name, domain_dict)

# pprint.pprint(db_config)

for table_name, table in S.puml_tables.items():
    for t in ("default", "primary", "foreign"):
        for fk in table[t].keys():
            logger.debug(f"{table_name}, {t}, {fk}")

puml_file = os.path.join(OUTPUT_DIR, "ER-GCOVER.puml")
logger.info(f"Writing PUML diagram to {puml_file}")

with open(puml_file, "w") as f:
    f.write(SP.transform())

yaml_file = os.path.join(OUTPUT_DIR, "GCOVERP.yaml")
logger.info(f"Writing YAML structure to {yaml_file}")
with open(yaml_file, "w") as f:
    yaml.dump(
        db_config,
        f,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        encoding=("utf-8"),
    )
