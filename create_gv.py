#!/usr/bin/env python3

import os
import sys
import json

import yaml

from loguru import logger

from sql2puml import SQL2PUML

FONTNAME = "DejaVu Sans,Nimbus Sans"

OUTPUT_DIR = "outputs"

logger.remove(0)
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")

# https://coolors.co/palette/ccd5ae-e9edc9-fefae0-faedcd-d4a373

data = {
    "bg_color": "#FEFAE0",
    "table_color": "#CCD5AE",
    "table_bg": "#E9EDC9",
    "class_bg": "#FAEDCD",
    "class_color": "#D4A373",
    "rectangle_color": "CD5656",
}  # without #


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
# input_file = "inputs/geocover-schema-sde.json"

input_file = "exports_i/gcoveri_simple.json"

basename = os.path.splitext(os.path.basename(input_file))[0]


output_file = os.path.join(OUTPUT_DIR, basename + ".png")
dotfile = os.path.join(OUTPUT_DIR, basename + ".dot")


with open(input_file, "r") as field_name:
    c = field_name.read()


db_schema = json.loads(c)

if db_schema.get("version") != 2:
    logger.error("Wrong schema version. Exiting...")
    sys.exit(2)

all_tables = {}

# SQL_graph = SQL2PUML(template_file="templates/template.puml", data=data)


for table_name in db_schema["tables"].keys():
    short_name = clean(table_name)
    if table_name.endswith("_I") or short_name in IGNORE_OBJECTS:
        continue

    logger.info(f"====Table {short_name}====")

    # SQL_graph.add_table(short_name)

    fields = db_schema["tables"][table_name].get(
        "fields", []
    )  # TODO shoud be fields: []

    table_object = Table(short_name)
    for field in fields:
        name = field.get("name")
        if name in IGNORE_FIELDS:
            continue
        typ = (
            field.get("domain")
            if field.get("domain") is not None
            else field.get("type")
        )
        # SQL_graph.add_column(name, typ)
        if name.lower() == "uuid":
            primary = True
        else:
            primary = False

        table_object.columns.append(Column(name, typ, primary=primary))
    all_tables[short_name] = table_object

    logger.info(table_object)


for field_name in db_schema["featclasses"].keys():
    short_name = clean(field_name)

    fields = db_schema["featclasses"][field_name]["fields"]

    if field_name.endswith("_I") or short_name in IGNORE_OBJECTS:
        logger.debug(short_name)
        continue
    logger.info(f"========FeatureClass {short_name}===============")

    # SQL_graph.add_table(short_name)
    featclass = FeatureClass(short_name, "Geometry")
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
        # SQL_graph.add_column(name, typ)
        featclass.columns.append(Column(name, typ, primary=primary))
    all_tables[short_name] = featclass


relations = [r for r in db_schema["relationships"].keys() if not r.endswith("_I")]

for i, r in enumerate(relations):
    cr = clean(r)

    rr = db_schema["relationships"][r]
    cardinality = rr["cardinality"]


for i, r in enumerate(relations):
    rr = db_schema["relationships"][r]
    cr = clean(r)
    short_name = clean(r)
    logger.info(f"======== Relationship {short_name}===============")
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

        logger.warning(
            f'Relationships "ManyToMany" {ori_table.name} --> {dest_table.name}'
        )

        table = Table(new_table, relation=True, cardinality="ManyToMany")
        # t.columns.append(Column(keys["origin"]["fk"], "int"))
        # t.columns.append(Column(keys["destination"]["fk"], "int"))
        all_tables[new_table] = table

        # fk = ColumnFK(name, type_, reference

        ori_pk = ori_table.get_column(keys["origin"]["pk"], erase=False)
        logger.debug(f"FK: {ori_pk}", [col.name for col in ori_table.columns], ori_pk)
        if ori_pk is not None:
            type_ = ori_pk.type_
            col = ColumnFK(keys["origin"]["fk"], type_, origin)
            table.columns.append(col)

        dest_pk = ori_table.get_column(keys["destination"]["pk"], erase=False)
        logger.debug(
            f"FK: {dest_pk}", [col.name for col in dest_table.columns], dest_pk
        )
        if dest_pk is not None:
            type_ = dest_pk.type_
            col = ColumnFK(keys["destination"]["fk"], type_, destination)
            table.columns.append(col)

        all_tables[destination] = table


db_config = {"database": "GCOVERP", "version": 1, "tables": []}

logger.info("-----------------------")

Sql2PUML = SQL2PUML(template_file="templates/template.puml", data=data)
for name, table in all_tables.items():
    if not name.startswith("GC_"):
        continue
    logger.info(f"===== TABLE: {name} =====")
    # logger.info()

    if Sql2PUML.puml_tables.get(name) is not None:
        Sql2PUML.current_table = name
    else:
        Sql2PUML.add_table(name)
    table_object = {"name": name, "columns": []}
    # pprint.pprint(table.columns)
    for col in table.columns:
        c = {}
        if isinstance(col, ColumnFK):
            logger.info("    {col.name} is foreign")
            Sql2PUML.add_column_foreign(col.name, col.type_, col.reference)
            c = {
                "foreign_key": {
                    "name": col.name,
                    "type": col.type_,
                    "reference": col.reference,
                }
            }

        else:
            if col.primary is True:
                logger.info(f"    PK: {col.name}")
                Sql2PUML.add_column_primary(col.name, col.type_)
            else:
                logger.info(f"    {col.name} is not foreign {type(col)}")
                Sql2PUML.add_column(col.name, col.type_)
            c = {"name": col.name, "type": col.type_, "primary_key": primary}
        table_object["columns"].append(c)
    db_config["tables"].append(table_object)

coded_domains = db_schema.get("coded_domain")
for name in coded_domains.keys():
    # logger.info(f"----{name}----")
    domain_dict = coded_domains[name]
    Sql2PUML.add_enum(name, domain_dict)

# pprint.pprint(db_config)

# Only debug?
# for table_name, table in SQL_graph.puml_tables.items():
#     for t in ("default", "primary", "foreign"):
#         for fk in table[t].keys():
#             logger.debug(f"{table_name}, {t}, {fk}")

puml_file = os.path.join(OUTPUT_DIR, "ER-GCOVER.puml")


with open(puml_file, "w") as field_name:
    field_name.write(Sql2PUML.transform())

yaml_file = os.path.join(OUTPUT_DIR, "GCOVERP.yaml")

with open(yaml_file, "w") as field_name:
    yaml.dump(
        db_config,
        field_name,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        encoding=("utf-8"),
    )

logger.debug(f"Template was: {Sql2PUML.puml_template}")

logger.info(f"Writing PUML diagram to {puml_file}")
logger.info(f"Writing YAML structure to {yaml_file}")
