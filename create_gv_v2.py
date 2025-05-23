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
        cleaned = s
        # cleaned = list(map(lambda x: x.replace("TOPGIS_GC.", ""), s))
        if len(cleaned) == 1:
            return cleaned[0]
        else:
            return cleaned
    else:
        return s
        # return s.replace("TOPGIS_GC.", "")


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
        "TOPGIS_GC.GC_ERRORS_ROW"
    ]
)

# Helper classes for better data organization
from collections import namedtuple

RelationshipInfo = namedtuple('RelationshipInfo', [
    'name', 'cardinality', 'origin_name', 'destination_name',
    'forward_label', 'origin_keys', 'destination_keys'
])

KeyMapping = namedtuple('KeyMapping', ['primary_key', 'foreign_key'])
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
    def __init__(self, name, relation=False, cardinality=None, is_spatial=False):
        self.name = name
        self.columns = []
        self.relation = relation
        self.cardinality = cardinality
        self.is_spatial = is_spatial

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
def process_database_tables(db_schema, ignore_objects, ignore_fields, logger):
    """
    Process database schema tables and feature classes, converting them to Table objects for PlantUML generation.

    Args:
        db_schema: Database schema JSON containing table and featureclass definitions
        ignore_objects: Set of table names to skip during processing
        ignore_fields: Set of field names to skip during processing
        logger: Logger instance for debugging output

    Returns:
        dict: Dictionary mapping table names to Table objects
    """
    processed_tables = {}

    # Process regular tables
    if "tables" in db_schema:
        _process_table_collection(
            db_schema["tables"],
            processed_tables,
            ignore_objects,
            ignore_fields,
            logger,
            is_spatial=False
        )

    # Process spatial feature classes
    if "featclasses" in db_schema:
        _process_table_collection(
            db_schema["featclasses"],
            processed_tables,
            ignore_objects,
            ignore_fields,
            logger,
            is_spatial=True
        )

    return processed_tables


def _process_table_collection(table_collection, processed_tables, ignore_objects, ignore_fields, logger,
                              is_spatial=False):
    """Process a collection of tables or feature classes."""
    table_type = "Feature Class" if is_spatial else "Table"

    for raw_table_name in table_collection.keys():
        clean_table_name = clean(raw_table_name)

        if _should_skip_table(raw_table_name, clean_table_name, ignore_objects):
            continue

        logger.info(f"====Processing {table_type}: {clean_table_name}====")

        table_fields = table_collection[raw_table_name].get("fields", [])
        table_object = _create_table_with_columns(clean_table_name, table_fields, ignore_fields, is_spatial)

        processed_tables[clean_table_name] = table_object
        logger.info(table_object)


def _should_skip_table(raw_table_name, clean_table_name, ignore_objects):
    """Check if a table should be skipped based on naming conventions or ignore list."""
    is_internal_table = raw_table_name.endswith("_I")
    is_ignored_table = clean_table_name in ignore_objects
    return is_internal_table or is_ignored_table


def _create_table_with_columns(table_name, table_fields, ignore_fields, is_spatial=False):
    """Create a Table object and populate it with processed columns."""
    # Create table with spatial indicator if it's a feature class
    table_object = Table(table_name, is_spatial=is_spatial) if is_spatial else Table(table_name)

    for field_definition in table_fields:
        column = _process_table_field(field_definition, ignore_fields, is_spatial)
        if column:  # Only add if field wasn't ignored
            table_object.columns.append(column)

    return table_object


def _process_table_field(field_definition, ignore_fields, is_spatial=False):
    """
    Process a single table field and convert it to a Column object.

    Args:
        field_definition: Dictionary containing field information
        ignore_fields: Set of field names to skip
        is_spatial: Boolean indicating if this is a spatial feature class

    Returns:
        Column object if field should be included, None if field should be ignored
    """
    field_name = field_definition.get("name")

    if field_name in ignore_fields:
        return None

    # Use domain if available, otherwise fall back to type
    field_type = (
        field_definition.get("domain")
        if field_definition.get("domain") is not None
        else field_definition.get("type")
    )

    # Check for primary key (UUID field)
    is_primary_key = field_name.lower() == "uuid"

    # Check if this is a geometry field (common in feature classes)
    is_geometry_field = (
            is_spatial and
            field_type and
            ("geometry" in field_type.lower() or "shape" in field_name.lower())
    )

    # Mark geometry fields differently for PlantUML visualization
    if is_geometry_field:
        field_type = f"[GEOMETRY] {field_type}"

    return Column(field_name, field_type, primary=is_primary_key)


def process_database_relationships(db_schema, all_tables, logger):
    """
    Process database relationships and update table objects with foreign keys.
    Creates junction tables for ManyToMany relationships and adds foreign keys for OneToMany.

    Args:
        db_schema: Database schema JSON containing relationship definitions
        all_tables: Dictionary of existing Table objects (modified in-place)
        logger: Logger instance for debugging output

    Returns:
        dict: Updated all_tables dictionary with relationship information
    """
    if "relationships" not in db_schema:
        logger.info("No relationships found in schema")
        return all_tables

    valid_relationships = _get_valid_relationships(db_schema)
    logger.info(f"Found {len(valid_relationships)} valid relationships to process")

    for relationship_index, relationship_name in enumerate(valid_relationships):
        relationship_data = db_schema["relationships"][relationship_name]
        clean_relationship_name = clean(relationship_name)

        logger.info(
            f"------- Processing Relationship {relationship_index + 1}/{len(valid_relationships)}: {clean_relationship_name} ----------")
        logger.info(f"Cardinality: {relationship_data.get('cardinality', 'Unknown')}")

        _process_single_relationship(
            relationship_data,
            clean_relationship_name,
            relationship_index,
            all_tables,
            logger
        )

    return all_tables


def _get_valid_relationships(db_schema):
    """Filter out internal relationships (ending with '_I')."""
    return [
        relationship_name
        for relationship_name in db_schema["relationships"].keys()
        if not relationship_name.endswith("_I")
    ]


def _process_single_relationship(relationship_data, relationship_name, relationship_index, all_tables, logger):
    """Process a single relationship based on its cardinality type."""
    cardinality = relationship_data["cardinality"]
    origin_table_name = clean(relationship_data["origin"])
    destination_table_name = clean(relationship_data["destination"])

    relationship_info = RelationshipInfo(
        name=relationship_name,
        cardinality=cardinality,
        origin_name=origin_table_name,
        destination_name=destination_table_name,
        forward_label=relationship_data.get("forwardPathLabel", str(relationship_index)),
        origin_keys=relationship_data.get("originClassKeys", []),
        destination_keys=relationship_data.get("destinationClassKeys", [])
    )

    logger.info(f"  Origin: {origin_table_name} -> Destination: {destination_table_name}")

    if "OneToMany" in cardinality:
        _handle_one_to_many_relationship(relationship_info, all_tables, logger)
    elif "ManyToMany" in cardinality:
        _handle_many_to_many_relationship(relationship_info, all_tables, logger)
    elif "OneToOne" in cardinality:
        _handle_one_to_one_relationship(relationship_info, all_tables, logger)
    else:
        logger.warning(f"Unsupported cardinality type: {cardinality} for relationship {relationship_name}")


def _handle_one_to_one_relationship(relationship_info, all_tables, logger):
    """Handle OneToOne relationship - similar to OneToMany but with different constraints."""
    logger.info("  Processing One-to-One relationship")
    # For now, treat similar to OneToMany - you might want different logic here
    _handle_one_to_many_relationship(relationship_info, all_tables, logger)


def _handle_one_to_many_relationship(relationship_info, all_tables, logger):
    """Handle OneToMany relationship by adding foreign key to destination table."""
    logger.info("  Processing One-to-Many relationship")

    origin_table = all_tables.get(relationship_info.origin_name)
    destination_table = all_tables.get(relationship_info.destination_name)

    if not origin_table or not destination_table:
        logger.error(
            f"Missing table(s): origin={relationship_info.origin_name}, dest={relationship_info.destination_name}")
        return

    key_mapping = _extract_key_mapping(relationship_info.origin_keys, logger)
    if not key_mapping:
        return

    # Get the primary key column from origin table to determine foreign key type
    primary_key_column = origin_table.get_column(key_mapping.primary_key, erase=False)
    if not primary_key_column:
        logger.error(f"Primary key '{key_mapping.primary_key}' not found in origin table")
        return

    # Add foreign key column to destination table
    foreign_key_column = ColumnFK(
        name=key_mapping.foreign_key,
        type_=primary_key_column.type_,
        reference=relationship_info.origin_name
    )
    destination_table.columns.append(foreign_key_column)
    all_tables[relationship_info.destination_name] = destination_table

    logger.debug(f"Added FK: {key_mapping.foreign_key} -> {relationship_info.origin_name}")


def _handle_many_to_many_relationship(relationship_info, all_tables, logger):
    """Handle ManyToMany relationship by creating junction table."""
    junction_table_name = f"{relationship_info.origin_name}_{relationship_info.destination_name}"
    logger.info(f"  Processing Many-to-Many relationship")
    logger.info(f"  Creating junction table: '{junction_table_name}'")

    if junction_table_name in all_tables:
        logger.info(f'  Junction table "{junction_table_name}" already exists - skipping')
        return

    origin_table = all_tables.get(relationship_info.origin_name)
    destination_table = all_tables.get(relationship_info.destination_name)

    if not origin_table:
        logger.warning(f"  Origin table '{relationship_info.origin_name}' not found")
        return

    if not destination_table:
        logger.warning(f"  Destination table '{relationship_info.destination_name}' not found")
        return

    # Extract key information for both sides of the relationship
    origin_key_mapping = _extract_key_mapping(relationship_info.origin_keys, logger, "origin")
    destination_key_mapping = _extract_key_mapping(relationship_info.destination_keys, logger, "destination")

    # Create junction table
    junction_table = Table(junction_table_name, relation=True, cardinality="ManyToMany")

    # Add foreign key columns from both tables
    success_origin = _add_foreign_key_to_junction_table(
        junction_table, origin_table, origin_key_mapping,
        relationship_info.origin_name, relationship_info.origin_keys, logger, "origin"
    )

    success_destination = _add_foreign_key_to_junction_table(
        junction_table, destination_table, destination_key_mapping,
        relationship_info.destination_name, relationship_info.destination_keys, logger, "destination"
    )

    if success_origin or success_destination:
        all_tables[junction_table_name] = junction_table
        logger.info(f"  Successfully created junction table: {junction_table_name}")
    else:
        logger.error(f"  Failed to create junction table: {junction_table_name} - no valid foreign keys found")


def _add_foreign_key_to_junction_table(junction_table, source_table, key_mapping, source_table_name, source_keys,
                                       logger, table_role):
    """Add a foreign key column to the junction table from a source table."""
    if not source_table:
        logger.warning(f"  {table_role.capitalize()} table '{source_table_name}' not found")
        return False

    if not key_mapping:
        logger.warning(f"  No key mapping found for {table_role} table '{source_table_name}'")
        return False

    primary_key_column = source_table.get_column(key_mapping.primary_key, erase=False)
    if not primary_key_column:
        logger.warning(
            f"  Primary key '{key_mapping.primary_key}' not found in {table_role} table '{source_table_name}'")
        return False

    # Look for specific foreign key name in the relationship keys
    foreign_key_name = _find_foreign_key_name(source_keys)
    if not foreign_key_name:
        foreign_key_name = key_mapping.foreign_key

    if foreign_key_name:
        foreign_key_column = ColumnFK(
            name=foreign_key_name,
            type_=primary_key_column.type_,
            reference=source_table_name
        )
        junction_table.columns.append(foreign_key_column)
        logger.debug(f"  Added FK to junction table: {foreign_key_name} -> {source_table_name}")
        return True
    else:
        logger.warning(f"  No foreign key name found for {table_role} table '{source_table_name}'")
        return False


def _find_foreign_key_name(relationship_keys):
    """Find the foreign key name from relationship key definitions."""
    for key_def in relationship_keys:
        key_role = key_def.get("keyRole", "")
        if "esriRelKeyRoleOriginForeign" in key_role:
            return key_def.get("objectKeyName")
    return None


def _extract_key_mapping(key_definitions, logger, table_role=""):
    """
    Extract primary and foreign key names from relationship key definitions.

    Args:
        key_definitions: List of key definition dictionaries
        logger: Logger instance
        table_role: String describing the table role (for better error messages)

    Returns:
        KeyMapping namedtuple or None if keys couldn't be extracted
    """
    if not key_definitions:
        logger.error(f"  No key definitions provided for {table_role} table")
        return None

    primary_key = None
    foreign_key = None

    for key_def in key_definitions:
        key_role = key_def.get("keyRole", "")
        key_name = key_def.get("objectKeyName", "")

        if "Primary" in key_role:
            primary_key = key_name
        elif "Foreign" in key_role:
            foreign_key = key_name
        else:
            # If role is not explicitly Primary/Foreign, use the key name as foreign key
            if not foreign_key:
                foreign_key = key_name

    if not primary_key and not foreign_key:
        logger.error(f"  No valid keys found for {table_role} table - Primary: {primary_key}, Foreign: {foreign_key}")
        return None

    # If we have primary key but no foreign key, use primary key name as foreign key base
    if primary_key and not foreign_key:
        foreign_key = primary_key

    logger.debug(f"  Extracted keys for {table_role}: Primary='{primary_key}', Foreign='{foreign_key}'")
    return KeyMapping(primary_key=primary_key, foreign_key=foreign_key)


# Helper classes for better data organization
from collections import namedtuple

RelationshipInfo = namedtuple('RelationshipInfo', [
    'name', 'cardinality', 'origin_name', 'destination_name',
    'forward_label', 'origin_keys', 'destination_keys'
])

KeyMapping = namedtuple('KeyMapping', ['primary_key', 'foreign_key'])

from pprint import pprint
all_tables = process_database_tables(db_schema, IGNORE_OBJECTS, IGNORE_FIELDS, logger)


all_tables  = process_database_relationships(db_schema, all_tables, logger)

pprint(all_tables)
sys.exit()





db_config = {"database": "GCOVERP", "version": 1, "tables": []}

logger.info("------------ttt-----------")


Sql2PUML = SQL2PUML(template_file="templates/template.puml", data=data)
for name, table in all_tables.items():
    if "GC_" not in name:
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
            logger.info(f"    {col.name} is foreign {col.reference}")
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
                primary = True
            else:
                logger.info(f"    {col.name}")
                Sql2PUML.add_column(col.name, col.type_)
                primary = False
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

# TOPGIS_GC.GC_BEDROCK "0..n" -- "1..1" TOPGIS_GC.GC_GEOL_MAPPING_UNIT_ATT
# class(TOPGIS_GC.GC_BEDROCK) {
# 	foreign_key(GEOL_MAPPING_UNIT_ATT_UUID,TOPGIS_GC.GC_GEOL_MAPPING_UNIT_ATT) GUID
# }
