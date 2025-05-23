#!/usr/bin/env python3

import os
import sys
import json

import yaml

from loguru import logger

from sql2puml import SQL2PUML
from typing import Union, List


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


def remove_prefix(
    text: Union[str, List[str]], prefix: str = "TOPGIS_GC."
) -> Union[str, List[str]]:
    """
    Remove a prefix from a string or list of strings while preserving the original type.

    Args:
        text: String or list of strings to process
        prefix: Prefix to remove (default: "TOPGIS_GC.")

    Returns:
        Cleaned string or list of strings with prefix removed
    """

    def _remove_single_prefix(s: str) -> str:
        return s[len(prefix) :] if s.startswith(prefix) else s

    if isinstance(text, str):
        return _remove_single_prefix(text)
    elif isinstance(text, list):
        cleaned = [_remove_single_prefix(s) for s in text]
        return cleaned[0] if len(cleaned) == 1 else cleaned
    else:
        return text


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


IGNORE_OBJECTS = remove_prefix(
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
        "TOPGIS_GC.GC_ERRORS_ROW",
    ]
)

# Helper classes for better data organization
from collections import namedtuple

RelationshipInfo = namedtuple(
    "RelationshipInfo",
    [
        "name",
        "cardinality",
        "origin_name",
        "destination_name",
        "forward_label",
        "origin_keys",
        "destination_keys",
    ],
)

KeyMapping = namedtuple("KeyMapping", ["primary_key", "foreign_key"])


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
            is_spatial=False,
        )

    # Process spatial feature classes
    if "featclasses" in db_schema:
        _process_table_collection(
            db_schema["featclasses"],
            processed_tables,
            ignore_objects,
            ignore_fields,
            logger,
            is_spatial=True,
        )

    return processed_tables


def _process_table_collection(
    table_collection,
    processed_tables,
    ignore_objects,
    ignore_fields,
    logger,
    is_spatial=False,
):
    """Process a collection of tables or feature classes."""
    table_type = "Feature Class" if is_spatial else "Table"

    for raw_table_name in table_collection.keys():
        clean_table_name = remove_prefix(raw_table_name)  # was clean

        if _should_skip_table(raw_table_name, clean_table_name, ignore_objects):
            continue

        logger.info(f"====Processing {table_type}: {clean_table_name}====")

        table_fields = table_collection[raw_table_name].get("fields", [])
        table_object = _create_table_with_columns(
            clean_table_name, table_fields, ignore_fields, is_spatial
        )

        processed_tables[clean_table_name] = table_object
        logger.info(table_object)


def _should_skip_table(raw_table_name, clean_table_name, ignore_objects):
    """Check if a table should be skipped based on naming conventions or ignore list."""
    is_internal_table = raw_table_name.endswith("_I")
    is_ignored_table = clean_table_name in ignore_objects
    return is_internal_table or is_ignored_table


def _create_table_with_columns(
    table_name, table_fields, ignore_fields, is_spatial=False
):
    """Create a Table object and populate it with processed columns."""
    # Create table with spatial indicator if it's a feature class
    table_object = (
        Table(table_name, is_spatial=is_spatial) if is_spatial else Table(table_name)
    )

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
        is_spatial
        and field_type
        and ("geometry" in field_type.lower() or "shape" in field_name.lower())
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
            f"------- Processing Relationship {relationship_index + 1}/{len(valid_relationships)}: {clean_relationship_name} ----------"
        )
        logger.info(f"Cardinality: {relationship_data.get('cardinality', 'Unknown')}")

        _process_single_relationship(
            relationship_data,
            clean_relationship_name,
            relationship_index,
            all_tables,
            logger,
        )

    return all_tables


def _get_valid_relationships(db_schema):
    """Filter out internal relationships (ending with '_I')."""
    return [
        relationship_name
        for relationship_name in db_schema["relationships"].keys()
        if not relationship_name.endswith("_I")
    ]


def _process_single_relationship(
    relationship_data, relationship_name, relationship_index, all_tables, logger
):
    """Process a single relationship based on its cardinality type."""
    cardinality = relationship_data["cardinality"]
    origin_table_name = remove_prefix(relationship_data["origin"])
    destination_table_name = remove_prefix(relationship_data["destination"])

    relationship_info = RelationshipInfo(
        name=relationship_name,
        cardinality=cardinality,
        origin_name=origin_table_name,
        destination_name=destination_table_name,
        forward_label=relationship_data.get(
            "forwardPathLabel", str(relationship_index)
        ),
        origin_keys=relationship_data.get("originClassKeys", []),
        destination_keys=relationship_data.get("destinationClassKeys", []),
    )

    logger.info(
        f"  Origin: {origin_table_name} -> Destination: {destination_table_name}"
    )

    if "OneToMany" in cardinality:
        _handle_one_to_many_relationship(relationship_info, all_tables, logger)
    elif "ManyToMany" in cardinality:
        _handle_many_to_many_relationship(relationship_info, all_tables, logger)
    elif "OneToOne" in cardinality:
        _handle_one_to_one_relationship(relationship_info, all_tables, logger)
    else:
        logger.warning(
            f"Unsupported cardinality type: {cardinality} for relationship {relationship_name}"
        )


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
            f"Missing table(s): origin={relationship_info.origin_name}, dest={relationship_info.destination_name}"
        )
        return

    key_mapping = _extract_key_mapping(relationship_info.origin_keys, logger)
    if not key_mapping:
        return

    # Get the primary key column from origin table to determine foreign key type
    primary_key_column = origin_table.get_column(key_mapping.primary_key, erase=False)
    if not primary_key_column:
        logger.error(
            f"Primary key '{key_mapping.primary_key}' not found in origin table"
        )
        return

    # Add foreign key column to destination table
    foreign_key_column = ColumnFK(
        name=key_mapping.foreign_key,
        type_=primary_key_column.type_,
        reference=relationship_info.origin_name,
    )
    destination_table.columns.append(foreign_key_column)
    all_tables[relationship_info.destination_name] = destination_table

    logger.debug(
        f"Added FK: {key_mapping.foreign_key} -> {relationship_info.origin_name}"
    )


def _handle_many_to_many_relationship(relationship_info, all_tables, logger):
    """Handle ManyToMany relationship by creating junction table."""
    junction_table_name = (
        f"{relationship_info.origin_name}_{relationship_info.destination_name}"
    )
    logger.info(f"  Processing Many-to-Many relationship")
    logger.info(f"  Creating junction table: '{junction_table_name}'")

    if junction_table_name in all_tables:
        logger.info(
            f'  Junction table "{junction_table_name}" already exists - skipping'
        )
        return

    origin_table = all_tables.get(relationship_info.origin_name)
    destination_table = all_tables.get(relationship_info.destination_name)

    if not origin_table:
        logger.warning(f"  Origin table '{relationship_info.origin_name}' not found")
        return

    if not destination_table:
        logger.warning(
            f"  Destination table '{relationship_info.destination_name}' not found"
        )
        return

    # Extract key information for both sides of the relationship
    origin_key_mapping = _extract_key_mapping(
        relationship_info.origin_keys, logger, "origin"
    )
    destination_key_mapping = _extract_key_mapping(
        relationship_info.destination_keys, logger, "destination"
    )

    # Create junction table
    junction_table = Table(junction_table_name, relation=True, cardinality="ManyToMany")

    # Add foreign key columns from both tables
    success_origin = _add_foreign_key_to_junction_table(
        junction_table,
        origin_table,
        origin_key_mapping,
        relationship_info.origin_name,
        relationship_info.origin_keys,
        logger,
        "origin",
    )

    success_destination = _add_foreign_key_to_junction_table(
        junction_table,
        destination_table,
        destination_key_mapping,
        relationship_info.destination_name,
        relationship_info.destination_keys,
        logger,
        "destination",
    )

    if success_origin or success_destination:
        all_tables[junction_table_name] = junction_table
        logger.info(f"  Successfully created junction table: {junction_table_name}")
    else:
        logger.error(
            f"  Failed to create junction table: {junction_table_name} - no valid foreign keys found"
        )


def _add_foreign_key_to_junction_table(
    junction_table,
    source_table,
    key_mapping,
    source_table_name,
    source_keys,
    logger,
    table_role,
):
    """Add a foreign key column to the junction table from a source table."""
    if not source_table:
        logger.warning(
            f"  {table_role.capitalize()} table '{source_table_name}' not found"
        )
        return False

    if not key_mapping:
        logger.warning(
            f"  No key mapping found for {table_role} table '{source_table_name}'"
        )
        return False

    primary_key_column = source_table.get_column(key_mapping.primary_key, erase=False)
    if not primary_key_column:
        logger.warning(
            f"  Primary key '{key_mapping.primary_key}' not found in {table_role} table '{source_table_name}'"
        )
        return False

    # Look for specific foreign key name in the relationship keys
    foreign_key_name = _find_foreign_key_name(source_keys)
    if not foreign_key_name:
        foreign_key_name = key_mapping.foreign_key

    if foreign_key_name:
        foreign_key_column = ColumnFK(
            name=foreign_key_name,
            type_=primary_key_column.type_,
            reference=source_table_name,
        )
        junction_table.columns.append(foreign_key_column)
        logger.debug(
            f"  Added FK to junction table: {foreign_key_name} -> {source_table_name}"
        )
        return True
    else:
        logger.warning(
            f"  No foreign key name found for {table_role} table '{source_table_name}'"
        )
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
        logger.error(
            f"  No valid keys found for {table_role} table - Primary: {primary_key}, Foreign: {foreign_key}"
        )
        return None

    # If we have primary key but no foreign key, use primary key name as foreign key base
    if primary_key and not foreign_key:
        foreign_key = primary_key

    logger.debug(
        f"  Extracted keys for {table_role}: Primary='{primary_key}', Foreign='{foreign_key}'"
    )
    return KeyMapping(primary_key=primary_key, foreign_key=foreign_key)


# Helper classes for better data organization
from collections import namedtuple

RelationshipInfo = namedtuple(
    "RelationshipInfo",
    [
        "name",
        "cardinality",
        "origin_name",
        "destination_name",
        "forward_label",
        "origin_keys",
        "destination_keys",
    ],
)

KeyMapping = namedtuple("KeyMapping", ["primary_key", "foreign_key"])


def generate_puml_diagram(
    all_tables, diagram_title="Database Schema", logger=None, **kwargs
):
    """
    Generate PlantUML diagram from processed database tables with configurable styling.

    Args:
        all_tables: Dictionary of table_name -> Table objects
        diagram_title: Title for the PlantUML diagram
        logger: Optional logger for debugging
        **kwargs: Styling parameters (colors, fonts, etc.)

    Returns:
        str: Complete PlantUML diagram as string
    """
    if logger:
        logger.info(f"Generating PlantUML diagram for {len(all_tables)} tables")

    puml_lines = []

    # Generate header with styling config
    header_lines, config = _generate_header(diagram_title, **kwargs)
    puml_lines.extend(header_lines)

    # Generate table definitions
    for table_name, table_object in all_tables.items():
        table_puml = _generate_table_definition(table_name, table_object, config)
        puml_lines.extend(table_puml)
        puml_lines.append("")

    # Generate relationships
    relationship_lines = _generate_relationships(all_tables)
    puml_lines.extend(relationship_lines)

    # Ugly, end rectangle
    puml_lines.append("}")

    # PlantUML footer
    puml_lines.append("@enduml")

    diagram = "\n".join(puml_lines)

    if logger:
        logger.info("PlantUML diagram generation completed")

    return diagram


def _generate_header(diagram_title, **kwargs):
    """Generate PlantUML header with customizable styling parameters."""
    defaults = {
        "font_size": 10,
        "line_type": "ortho",
        "line_color": "#E1F5FE",
        "font_color": "#E1F5FE",
        "theme": "plain",
        "regular_table_color": "#E1F5FE",
        "spatial_table_color": "#E8F5E8",
        "junction_table_color": "#FFF8E1",
        "relation_table_color": "#F3E5F5",
        "bg_color": "#F3E5F5",
    }

    config = {**defaults, **kwargs}

    header_lines = [
        "@startuml",
        f"!theme {config['theme']}",
        "",
        f"skinparam linetype {config['line_type']}",
        f"skinparam defaultFontSize {config['font_size']}",
        "skinparam rectangle {",
        "  roundCorner 50",
        f"  BackGroundColor {config['bg_color']}",
        "  LineThickness 10",
        f"  LineColor {config['line_color']}",
        "}",
        "",
        f"skinparam TitlefontColor  {config['line_color']}",
        f"skinparam TitleFontSize {config['font_size'] * 3}",
        "",
        "scale 1",
        "",
        f"rectangle   {config['bg_color']};line:CD5656;line.bold; {{",
    ]

    if config.get("bg_color"):
        header_lines.append(f"skinparam backgroundColor {config['bg_color']}")

    header_lines.extend(["", f"title {diagram_title}", ""])

    return header_lines, config


def _generate_table_definition(table_name, table_object, config):
    """Generate PlantUML definition for a single table with configurable colors."""
    lines = []

    display_name = _clean_table_name_for_display(table_name)
    alias_name = _clean_table_name_for_alias(table_name)

    # Apply configurable colors based on table type
    if hasattr(table_object, "relation") and table_object.relation:
        if (
            hasattr(table_object, "cardinality")
            and table_object.cardinality == "ManyToMany"
        ):
            lines.append(
                f"entity \"{display_name}\" as {alias_name} <<junction>> {config['junction_table_color']} {{"
            )
        else:
            lines.append(
                f"entity \"{display_name}\" as {alias_name} <<relation>> {config['relation_table_color']} {{"
            )
    elif hasattr(table_object, "is_spatial") and table_object.is_spatial:
        lines.append(
            f"entity \"{display_name} 🗺️\" as {alias_name} <<spatial>> {config['spatial_table_color']} {{"
        )
    else:
        lines.append(
            f"entity \"{display_name} 📋\" as {alias_name} {config['regular_table_color']} {{"
        )

    # Add columns
    if hasattr(table_object, "columns") and table_object.columns:
        primary_keys = []
        foreign_keys = []
        geometry_columns = []
        regular_columns = []

        for column in table_object.columns:
            if getattr(column, "primary", False):
                primary_keys.append(column)
            elif hasattr(column, "reference"):
                foreign_keys.append(column)
            elif (
                hasattr(column, "type_")
                and column.type_
                and "[GEOMETRY]" in str(column.type_)
            ):
                geometry_columns.append(column)
            else:
                regular_columns.append(column)

        all_ordered_columns = (
            primary_keys + regular_columns + geometry_columns + foreign_keys
        )

        if primary_keys:
            lines.append("  --")

        for column in all_ordered_columns:
            column_line = _format_column_definition(column)
            lines.append(f"  {column_line}")

            if column in primary_keys and (
                regular_columns or geometry_columns or foreign_keys
            ):
                lines.append("  --")
            elif column in geometry_columns and foreign_keys:
                lines.append("  --")
    else:
        lines.append("  -- No columns defined --")

    lines.append("}")
    return lines


def _format_column_definition(column):
    """Format a single column definition for PlantUML with enhanced styling."""
    name = getattr(column, "name", "unknown")
    type_ = getattr(column, "type_", "unknown")
    is_primary = getattr(column, "primary", False)
    is_foreign_key = hasattr(column, "reference")

    display_type = type_.replace("[GEOMETRY] ", "") if type_ else "unknown"

    if is_primary:
        return f"🔑 **{name}** : {display_type} <<PK>>"
    elif is_foreign_key:
        reference = getattr(column, "reference", "unknown")
        clean_reference = _clean_table_name_for_display(reference)
        return f"🔗 {name} : {display_type} <<FK➜{clean_reference}>>"
    else:
        if type_ and "[GEOMETRY]" in str(type_):
            return f"🗺️ {name} : {display_type} <<GEOMETRY>>"
        elif name.lower() in ["created_at", "updated_at", "date", "timestamp"]:
            return f"🕐 {name} : {display_type}"
        elif name.lower() in ["email", "mail"]:
            return f"📧 {name} : {display_type}"
        elif name.lower() in ["phone", "telephone", "mobile"]:
            return f"📱 {name} : {display_type}"
        elif name.lower() in ["url", "website", "link"]:
            return f"🌐 {name} : {display_type}"
        elif "status" in name.lower() or "state" in name.lower():
            return f"📊 {name} : {display_type}"
        else:
            return f"  {name} : {display_type}"


def _generate_relationships(all_tables):
    """Generate PlantUML relationship definitions with clean aliases."""
    relationship_lines = ["' Relationships"]
    processed_relationships = set()

    for table_name, table_object in all_tables.items():
        if not hasattr(table_object, "columns"):
            continue

        table_alias = _clean_table_name_for_alias(table_name)

        for column in table_object.columns:
            if hasattr(column, "reference"):
                reference_table = column.reference
                reference_alias = _clean_table_name_for_alias(reference_table)

                rel_id = f"{reference_alias}->{table_alias}"
                reverse_rel_id = f"{table_alias}->{reference_alias}"

                if (
                    rel_id not in processed_relationships
                    and reverse_rel_id not in processed_relationships
                ):
                    if hasattr(table_object, "relation") and table_object.relation:
                        if (
                            hasattr(table_object, "cardinality")
                            and table_object.cardinality == "ManyToMany"
                        ):
                            relationship_lines.append(
                                f'{reference_alias} ||--o{{ {table_alias} : "1:n"'
                            )
                        else:
                            relationship_lines.append(
                                f"{reference_alias} ||--|| {table_alias}"
                            )
                    else:
                        column_name = getattr(column, "name", "fk")
                        relationship_lines.append(
                            f'{reference_alias} ||--o{{ {table_alias} : "{column_name}"'
                        )

                    processed_relationships.add(rel_id)

    return relationship_lines


def _clean_table_name_for_display(table_name):
    """Clean table name for display by removing schema prefixes."""
    if "." in table_name:
        parts = table_name.split(".")
        if len(parts) >= 2 and parts[0].upper().startswith("TOPGIS"):
            return ".".join(parts[1:])
        elif len(parts) >= 2:
            return parts[-1]
    return table_name


def _clean_table_name_for_alias(table_name):
    """Clean table name for use as PlantUML alias."""
    clean_name = table_name.replace(".", "_").replace(" ", "_").replace("-", "_")
    return "".join(c for c in clean_name if c.isalnum() or c == "_")


def save_puml_diagram(
    all_tables,
    filename="database_schema.puml",
    diagram_title="Database Schema",
    logger=None,
    **kwargs,
):
    """Generate and save PlantUML diagram to file with custom styling."""
    puml_content = generate_puml_diagram(all_tables, diagram_title, logger, **kwargs)

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(puml_content)

        if logger:
            logger.info(f"PlantUML diagram saved to: {filename}")
    except Exception as e:
        if logger:
            logger.error(f"Failed to save PlantUML diagram: {e}")
        raise

    return puml_content


from pprint import pprint

all_tables = process_database_tables(db_schema, IGNORE_OBJECTS, IGNORE_FIELDS, logger)


all_tables = process_database_relationships(db_schema, all_tables, logger)

pprint(all_tables)

# coded_domains = process_coded_domains(db_schema, domain_prefix='GC_', logger=logger)
# pprint(coded_domains)
# Generate PlantUML diagram

diagram = generate_puml_diagram(all_tables, "My Database")

# Custom styling
diagram = generate_puml_diagram(
    all_tables,
    "Geocover 5.0 May 2025",
    font_size=12,
    spatial_table_color="#ECA77F",
    regular_table_color="#F4C8A6",
    theme="plain",
    bg_color="#F5DEBC",
)

with open("database_schema.puml", "w") as f:
    f.write(diagram)
# Or save to file
