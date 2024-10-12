import sys
import textwrap
from collections import OrderedDict

import openpyxl
import pandas as pd
import yaml
from loguru import logger
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from ruamel.yaml import YAML


class Datamodel:
    def __init__(self):
        self.yaml_data = OrderedDict()
        self.yaml_data["metadata"] = {}
        self.yaml_data["themes"] = []

    def import_from_excel(self, file_path):
        """Import data from an Excel file into the yaml_data structure."""
        # Load the workbook and the first sheet
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        yaml_data = OrderedDict()
        yaml_data["themes"] = []
        current_theme = None
        current_class = None

        n = 0
        revision = sheet["B2"].value
        revision_date = sheet["B3"].value
        schema_version = sheet["B3"].value

        yaml_data["model"] = {"revision": revision, "revision_date": revision_date}
        yaml_data["schema"] = str(schema_version)
        # Iterate over rows starting from the second row (skip headers)
        current_class_name = None
        current_class = None
        in_attributes = False
        for row in sheet.iter_rows(min_row=6, values_only=True):
            # Use the `or` operator to assign a default value (None or empty string) if the cell is empty

            if not any(row):
                continue

            n += 1
            theme_name = None
            class_name = None
            table_name = None
            abrev = None
            description_de = ""
            description_fr = ""
            attr_name = None
            attr_desc_de = attr_desc_fr = ""
            attr_type = mandatory = cardinality = None
            row_type = row[0] or ""
            if "Theme" in row_type:
                theme_name = row[1] or None
                in_attributes = False
            if "Class" in row_type:
                class_name = row[1] or None
                current_class_name = class_name
                in_attributes = False
            if "Description" in row_type:
                description_de = row[2] or ""
                description_fr = row[3] or ""
                in_attributes = False
            if "Abrev" in row_type:
                abrev = row[1] or None
                in_attributes = False
            if "Table" in row_type:
                table_name = row[1] or None
                in_attributes = False
            if "Attributes" in row_type:
                in_attributes = True
            if in_attributes:
                attr_name = row[1]
                attr_desc_de = row[2]
                attr_desc_fr = row[3]
                attr_type = row[4] or None
                mandatory = row[5] or "no"
                cardinality = row[6] or None

            # print(f"{row_type}, {attr_name}, in={in_attributes}")
            # print(row)
            # if n>20: return yaml_data

            # If a new theme is found
            if theme_name:
                # Create a new theme if it doesn't exist yet
                current_theme = {"name": theme_name, "classes": []}
                yaml_data["themes"].append(current_theme)

            # If a new class is found
            if class_name:
                # Create a new class if it doesn't exist yet
                current_class = {
                    "name": class_name,
                    "description": {
                        "de": description_de.strip(),
                        "fr": description_fr.strip(),
                    },
                    "attributes": [],
                }
                current_theme["classes"].append(current_class)
            if description_fr or description_de:
                current_class["description"]["de"] = "|" + description_de.strip()
                current_class["description"]["fr"] = "|" + description_fr.strip()
            if abrev:
                current_class["abrev"] = abrev
            if table_name:
                current_class["table"] = table_name

            # Add attribute to the current class
            if attr_name:
                attribute = {
                    "name": attr_name,
                    "att_type": attr_type,
                    "description": {"de": attr_desc_de, "fr": attr_desc_fr},
                    "mandatory": mandatory == "yes",
                    "cardinality": cardinality,
                }
                current_class["attributes"].append(attribute)
        self.yaml_data = yaml_data

        return yaml_data

    def export_to_excel(self, file_path):
        """Export the yaml_data structure to an Excel file."""
        yaml_data = self.yaml_data

        # Helper Functions
        def set_cell(worksheet, row, col, value, font=None, alignment=None, fill=None):
            cell = worksheet.cell(row=row, column=col, value=value)
            if font:
                cell.font = font
            if alignment:
                cell.alignment = alignment
            if fill:
                cell.fill = fill
            return cell

        def merge_and_format(worksheet, start_row, start_col, end_row, end_col, value, font):
            worksheet.merge_cells(start_row=start_row, start_column=start_col, end_row=end_row, end_column=end_col)
            cell = worksheet.cell(row=start_row, column=start_col)
            cell.value = value
            cell.font = font

        def update_row(worksheet, current_row, height=20):
            worksheet.row_dimensions[current_row].height = height
            return current_row + 1

        # Excel Writer
        with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
            worksheet = writer.book.create_sheet("Sheet1")

            # Title Section
            current_row = 1
            title_font = Font(size=20, bold=True, name="Arial")
            merge_and_format(worksheet, 1, 1, 1, 3, "Geology Data Model", title_font)
            worksheet.row_dimensions[current_row].height = 30

            # Metadata
            metadata_font = Font(size=12, bold=True, name="Arial")
            set_cell(worksheet, 2, 1, "Revision", metadata_font)
            set_cell(worksheet, 2, 2, yaml_data.get("model", {}).get("revision", ""), metadata_font)
            set_cell(worksheet, 3, 1, "Date", metadata_font)
            set_cell(worksheet, 3, 2, yaml_data.get("model", {}).get("revision_date", ""), metadata_font)
            set_cell(worksheet, 4, 1, "Schema", metadata_font)
            set_cell(worksheet, 4, 2, yaml_data.get("version", ""), metadata_font)

            # Header Section
            current_row = update_row(worksheet, current_row + 4)
            header_font = Font(size=14, bold=True, color="dddddd", name="Arial")
            header_alignment = Alignment(horizontal="center", vertical="center")
            header_fill = PatternFill(start_color="333333", end_color="dddddd", fill_type="solid")

            headers = ["Deutsch", "Français", "Type", "Mandatory", "Cardinality"]
            for i, header in enumerate(headers, start=3):
                set_cell(worksheet, current_row, i, header, font=header_font, alignment=header_alignment, fill=header_fill)

            current_row = update_row(worksheet, current_row)

            # Themes and Classes
            previous_theme = previous_class = previous_abrev = previous_table = previous_description_de = previous_description_fr = "dummy"
            for theme in yaml_data.get("themes", []):
                current_row = self._write_theme(worksheet, theme, current_row, set_cell, update_row)

                for cls in theme.get("classes", []):
                    current_row = self._write_class(worksheet, cls, current_row, set_cell, update_row)

            # Set column widths
            dim_holder = DimensionHolder(worksheet=worksheet)
            for col in range(worksheet.min_column, worksheet.max_column + 1):
                column_name = get_column_letter(col)
                width = 75 if column_name in ["C", "D"] else 20
                dim_holder[column_name] = ColumnDimension(worksheet, min=col, max=col, width=width)
            worksheet.column_dimensions = dim_holder

    def _write_theme(self, worksheet, theme, current_row, set_cell, update_row):
        """Private method to write theme data to the worksheet."""
        theme_name = theme.get("name", "")

        if theme_name:
            set_cell(worksheet, current_row, 1, "Theme", Font(bold=True, name="Arial"))
            set_cell(worksheet, current_row, 2, theme_name, Font(size=20, bold=True, name="Arial"))
            current_row = update_row(worksheet, current_row, height=30)
        
        return current_row

    def _write_class(self, worksheet, cls, current_row, set_cell, update_row):
        """Private method to write class data and its attributes to the worksheet."""
        class_name = cls.get("name", "")
        abrev = cls.get("abrev", "")
        table = cls.get("table", "")
        description_de = cls.get("description", {}).get("de", "")
        description_fr = cls.get("description", {}).get("fr", "")

        # Write Class details
        set_cell(worksheet, current_row, 1, "Class", Font(bold=True, name="Arial"))
        set_cell(worksheet, current_row, 2, class_name, Font(size=14, bold=True, name="Arial"))
        current_row = update_row(worksheet, current_row, height=20)

        # Description
        my_align = Alignment(wrapText=True, vertical="top")
        set_cell(worksheet, current_row, 1, "Description", Font(bold=True, name="Arial"), alignment=my_align)
        set_cell(worksheet, current_row, 3, description_de, alignment=my_align)
        set_cell(worksheet, current_row, 4, description_fr, alignment=my_align)
        current_row = update_row(worksheet, current_row, height=100)

        # Abbreviation and Table
        set_cell(worksheet, current_row, 1, "Abrev", Font(bold=True, name="Arial"))
        set_cell(worksheet, current_row, 2, abrev)
        current_row = update_row(worksheet, current_row)

        set_cell(worksheet, current_row, 1, "Table", Font(bold=True, name="Arial"))
        set_cell(worksheet, current_row, 2, table)
        current_row = update_row(worksheet, current_row)

        # Attributes
        set_cell(worksheet, current_row, 1, "Attributes", Font(bold=True, name="Arial"))
        current_row = update_row(worksheet, current_row)

        for attr in cls.get("attributes", []):
            attr_name = attr.get("name", "")
            attr_desc_de = attr.get("description", {}).get("de", "")
            attr_desc_fr = attr.get("description", {}).get("fr", "")
            attr_type = attr.get("att_type", "")
            mandatory = "yes" if attr.get("mandatory", False) else "no"
            cardinality = f"[{attr.get('cardinality', '')}]"

            # Write attribute details
            set_cell(worksheet, current_row, 2, attr_name.upper())
            set_cell(worksheet, current_row, 3, attr_desc_de, alignment=my_align)
            set_cell(worksheet, current_row, 4, attr_desc_fr, alignment=my_align)
            set_cell(worksheet, current_row, 5, attr_type)
            set_cell(worksheet, current_row, 6, mandatory)
            set_cell(worksheet, current_row, 7, cardinality)
            current_row = update_row(worksheet, current_row)

        current_row = update_row(worksheet, current_row, height=20)

        return current_row

    def export_to_yaml(self, file_path):
        """Export the yaml_data structure to a YAML file."""
        output_data = {
            key: dict(value) if isinstance(value, OrderedDict) else value
            for key, value in self.yaml_data.items()
        }
        with open(file_path, "w", encoding="utf-8") as yaml_file:
            yaml.dump(output_data, yaml_file, allow_unicode=True, sort_keys=False)

    def import_from_yaml(self, file_path):
        """Import data from a YAML file into the yaml_data structure."""
        with open(file_path, "r", encoding="utf-8") as yaml_file:
            self.yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)


if __name__ == "__main__":
    # Example Usage
    xlsx_file = "modelclass.xlsx"
    datamodel = Datamodel()
    datamodel.import_from_yaml("datamodel.yaml")
    logger.info(datamodel.yaml_data)

    logger.info("Export to Excel")
    # datamodel.export_to_yaml("output.yaml")
    datamodel.export_to_excel(xlsx_file)
    logger.info("Import from  Excel")
    datamodel.import_from_excel(xlsx_file)

    logger.info("Export to YAML")

    datamodel.export_to_yaml("modelclass.yaml")
