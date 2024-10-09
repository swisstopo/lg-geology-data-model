import openpyxl
import json

from ruamel.yaml import YAML

from collections import OrderedDict


def parse_excel_to_structure(file_path):
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
            current_class["description"]["de"] = description_de
            current_class["description"]["fr"] = description_fr
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

    return yaml_data


# Usage
file_path = "basic_excel.xlsx"
parsed_data = parse_excel_to_structure(file_path)
print(json.dumps(parsed_data, indent=4, default=str))

yaml = YAML()


output_data = {
    key: dict(value) if isinstance(value, OrderedDict) else value
    for key, value in parsed_data.items()
}

with open("basic_excel_back_runamel.yml", "w") as outfile:
    yaml.dump(parsed_data, outfile)

import yaml

with open("basic_excel_back.yml", "w", encoding="utf-8") as yaml_file:
    yaml.dump(output_data, yaml_file, allow_unicode=True, sort_keys=False)
