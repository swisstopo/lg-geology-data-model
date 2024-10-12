import json
from collections import OrderedDict
from datetime import date, datetime

import openpyxl
import pandas as pd
import yaml
from loguru import logger
from openpyxl.styles import Alignment, Font, PatternFill


from openpyxl.utils import get_column_letter
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder
from ruamel.yaml import YAML

DOCUMENT_TITLE = "Geology Data Model"

FONT_ARIAL_BOLD = Font(bold=True, name="Arial")
FONT_TITLE = Font(size=20, bold=True, name="Arial")
FONT_METADATA = Font(size=12, bold=True, name="Arial")
TEXT_WRAP_ALIGN_TOP = Alignment(wrapText=True, vertical="top")


def dequote(text):
    if text:
        text = " ".join(text.split())
        if text.startswith('"') and text.endswith('"'):
            text = string[1:-1]
    return text


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):  # Handles both datetime and date
            return obj.isoformat()  # or str(obj)
        return super().default(obj)


class Datamodel:
    def __init__(self):
        self.yaml_data = OrderedDict()
        self.yaml_data["metadata"] = {}
        self.yaml_data["themes"] = []

    def from_excel(self, file_path):
        """Import data from an Excel file into the yaml_data structure.

        Parameters
        ----------
        file_path
        """
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        self.yaml_data["themes"] = []
        current_theme = None
        current_class = None

        revision = sheet["B2"].value
        revision_date = sheet["B3"].value
        schema_version = sheet["B3"].value

        self.yaml_data["model"] = {"revision": revision, "revision_date": revision_date}
        self.yaml_data["schema"] = str(schema_version)

        in_attributes = False
        for row in sheet.iter_rows(min_row=6, values_only=True):
            if not any(row):
                continue

            row_type = row[0] or ""
            if "Theme" in row_type:
                theme_name = row[1] or None
                current_theme = self._create_new_theme(theme_name)
            if "Class" in row_type:
                class_name = row[1] or None
                current_class = self._create_new_class(class_name)
                current_theme["classes"].append(current_class)
            if "Description" in row_type:
                description_de = row[2] or ""
                description_fr = row[3] or ""
                self._update_class_description(
                    current_class, description_de, description_fr
                )
            if "Abrev" in row_type:
                abrev = row[1] or None
                current_class["abrev"] = abrev
            if "Table" in row_type:
                table_name = row[1] or None
                current_class["table"] = table_name
            if "Attributes" in row_type:
                in_attributes = True
            if (
                in_attributes and not row[0] and row[1]
            ):  # Check if attributes section and valid attribute
                self._add_attribute_to_class(current_class, row)

        return self.yaml_data

    def _create_new_theme(self, theme_name):
        """Create and return a new theme structure."""
        theme = {"name": theme_name, "classes": []}
        self.yaml_data["themes"].append(theme)
        return theme

    def _create_new_class(self, class_name):
        """Create and return a new class structure."""
        return {
            "name": class_name,
            "description": {"de": "", "fr": ""},
            "attributes": [],
        }

    def _update_class_description(self, current_class, description_de, description_fr):
        """Update the description of the current class."""
        current_class["description"]["de"] = dequote(description_de)
        current_class["description"]["fr"] = dequote(description_fr)

    def _add_attribute_to_class(self, current_class, row):
        """Add an attribute to the current class based on the row data."""
        attr_name = row[1] or None
        attr_desc_de = row[2] or ""
        attr_desc_fr = row[3] or ""
        attr_type = row[4] or None
        mandatory = row[5] or "no"
        cardinality = row[6] or None

        attribute = {
            "name": attr_name,
            "att_type": attr_type,
            "description": {"de": attr_desc_de, "fr": attr_desc_fr},
            "mandatory": mandatory == "yes",
            "cardinality": cardinality,
        }
        current_class["attributes"].append(attribute)

    def to_excel(self, file_path):
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

        def merge_and_format(
            worksheet, start_row, start_col, end_row, end_col, value, font
        ):
            worksheet.merge_cells(
                start_row=start_row,
                start_column=start_col,
                end_row=end_row,
                end_column=end_col,
            )
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

            merge_and_format(worksheet, 1, 1, 1, 3, DOCUMENT_TITLE, FONT_TITLE)
            worksheet.row_dimensions[current_row].height = 30

            # Metadata

            set_cell(worksheet, 2, 1, "Revision", FONT_METADATA)
            set_cell(
                worksheet,
                2,
                2,
                yaml_data.get("model", {}).get("revision", ""),
                FONT_METADATA,
            )
            set_cell(worksheet, 3, 1, "Date", FONT_METADATA)
            set_cell(
                worksheet,
                3,
                2,
                yaml_data.get("model", {}).get("revision_date", ""),
                FONT_METADATA,
            )
            set_cell(worksheet, 4, 1, "Schema", FONT_METADATA)
            set_cell(worksheet, 4, 2, yaml_data.get("version", ""), FONT_METADATA)

            # Header Section
            current_row = update_row(worksheet, current_row + 4)
            header_font = Font(size=14, bold=True, color="dddddd", name="Arial")
            header_alignment = Alignment(horizontal="center", vertical="center")
            header_fill = PatternFill(
                start_color="333333", end_color="dddddd", fill_type="solid"
            )

            headers = ["Deutsch", "Français", "Type", "Mandatory", "Cardinality"]
            for i, header in enumerate(headers, start=3):
                set_cell(
                    worksheet,
                    current_row,
                    i,
                    header,
                    font=header_font,
                    alignment=header_alignment,
                    fill=header_fill,
                )

            current_row = update_row(worksheet, current_row)

            # Themes and Classes
            previous_theme = previous_class = previous_abrev = previous_table = (
                previous_description_de
            ) = previous_description_fr = "dummy"
            for theme in yaml_data.get("themes", []):
                current_row = self._write_theme(
                    worksheet, theme, current_row, set_cell, update_row
                )

                for cls in theme.get("classes", []):
                    current_row = self._write_class(
                        worksheet, cls, current_row, set_cell, update_row
                    )

            # Set column widths
            dim_holder = DimensionHolder(worksheet=worksheet)
            for col in range(worksheet.min_column, worksheet.max_column + 1):
                column_name = get_column_letter(col)
                width = 75 if column_name in ["C", "D"] else 20
                dim_holder[column_name] = ColumnDimension(
                    worksheet, min=col, max=col, width=width
                )
            worksheet.column_dimensions = dim_holder

    def _write_theme(self, worksheet, theme, current_row, set_cell, update_row):
        """Private method to write theme data to the worksheet."""
        theme_name = theme.get("name", "")

        if theme_name:
            set_cell(worksheet, current_row, 1, "Theme", Font(bold=True, name="Arial"))
            set_cell(
                worksheet,
                current_row,
                2,
                theme_name,
                Font(size=20, bold=True, name="Arial"),
            )
            current_row = update_row(worksheet, current_row, height=30)

        return current_row

    def _write_class(self, worksheet, cls, current_row, set_cell, update_row):
        """Private method to write class data and its attributes to the worksheet."""
        class_name = cls.get("name", "")
        abrev = cls.get("abrev", "")
        table = cls.get("table", "")
        description_de = dequote(cls.get("description", {}).get("de", ""))
        description_fr = dequote(cls.get("description", {}).get("fr", ""))

        # Write Class details
        set_cell(worksheet, current_row, 1, "Class", FONT_ARIAL_BOLD)
        set_cell(
            worksheet,
            current_row,
            2,
            class_name,
            Font(size=14, bold=True, name="Arial"),
        )
        current_row = update_row(worksheet, current_row, height=20)

        # Description

        set_cell(
            worksheet,
            current_row,
            1,
            "Description",
            FONT_ARIAL_BOLD,
            alignment=TEXT_WRAP_ALIGN_TOP,
        )
        set_cell(
            worksheet, current_row, 3, description_de, alignment=TEXT_WRAP_ALIGN_TOP
        )
        set_cell(
            worksheet, current_row, 4, description_fr, alignment=TEXT_WRAP_ALIGN_TOP
        )
        current_row = update_row(worksheet, current_row, height=100)

        # Abbreviation and Table
        set_cell(worksheet, current_row, 1, "Abrev", FONT_ARIAL_BOLD)
        set_cell(worksheet, current_row, 2, abrev)
        current_row = update_row(worksheet, current_row)

        set_cell(worksheet, current_row, 1, "Table", FONT_ARIAL_BOLD)
        set_cell(worksheet, current_row, 2, table)
        current_row = update_row(worksheet, current_row)

        # Attributes
        set_cell(worksheet, current_row, 1, "Attributes", FONT_ARIAL_BOLD)
        current_row = update_row(worksheet, current_row)

        for attr in cls.get("attributes", []):
            attr_name = attr.get("name", "")
            attr_desc_de = attr.get("description", {}).get("de", "")
            attr_desc_fr = attr.get("description", {}).get("fr", "")
            attr_type = attr.get("att_type", "")
            mandatory = "yes" if attr.get("mandatory", False) else "no"
            cardinality = f"[{attr.get('cardinality', '')}]"

            # Write attribute details
            set_cell(
                worksheet,
                current_row,
                2,
                attr_name.upper(),
                alignment=TEXT_WRAP_ALIGN_TOP,
            )
            set_cell(
                worksheet, current_row, 3, attr_desc_de, alignment=TEXT_WRAP_ALIGN_TOP
            )
            set_cell(
                worksheet, current_row, 4, attr_desc_fr, alignment=TEXT_WRAP_ALIGN_TOP
            )
            set_cell(
                worksheet, current_row, 5, attr_type, alignment=TEXT_WRAP_ALIGN_TOP
            )
            set_cell(
                worksheet, current_row, 6, mandatory, alignment=TEXT_WRAP_ALIGN_TOP
            )
            set_cell(
                worksheet, current_row, 7, cardinality, alignment=TEXT_WRAP_ALIGN_TOP
            )
            current_row = update_row(worksheet, current_row)

        current_row = update_row(worksheet, current_row, height=20)

        return current_row

    def to_yaml(self, file_path):
        """Export the yaml_data structure to a YAML file."""
        yaml = YAML()
        output_data = {
            key: dict(value) if isinstance(value, OrderedDict) else value
            for key, value in self.yaml_data.items()
        }
        with open(file_path, "w") as yaml_file:
            yaml.dump(output_data, yaml_file)

    def from_yaml(self, file_path):
        """Import data from a YAML file into the yaml_data structure."""
        with open(file_path, "r", encoding="utf-8") as yaml_file:
            self.yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)


if __name__ == "__main__":
    # Example Usage
    xlsx_file = "modelclass.xlsx"
    datamodel = Datamodel()
    logger.info("Loading original model form YAML")
    datamodel.from_yaml("datamodel.yaml")
    logger.info(datamodel.yaml_data)

    logger.info(f"Export model to Excel: {xlsx_file}")
    # datamodel.export_to_yaml("output.yaml")
    datamodel.to_excel(xlsx_file)
    logger.info(f"Import from  Excel {xlsx_file}")
    datamodel.from_excel(xlsx_file)
    # logger.info(json.dumps(datamodel.yaml_data, indent=4, cls=DateTimeEncoder))

    logger.info("Export to YAML")

    datamodel.to_yaml("modelclass.yaml")
