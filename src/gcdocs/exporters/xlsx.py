"""
Excel exporter for gcdocs
Based on the model.py export functionality from original code
"""

import pandas as pd
from pathlib import Path
from loguru import logger
import yaml
from typing import Dict, Any, List


class XLSXExporter:
    """Export datamodel to Excel format"""

    def export(self, yaml_file: str, output_file: str):
        """Export YAML datamodel to Excel"""
        # Load YAML data
        with open(yaml_file, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)

        # Convert to Excel-friendly format
        excel_data = self._prepare_excel_data(yaml_data)

        # Write to Excel
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            self._write_excel_sheets(excel_data, writer)

        logger.info(f"Exported datamodel to {output_file}")

    def _prepare_excel_data(self, yaml_data: Dict[str, Any]) -> Dict[str, List[Dict]]:
        """Convert YAML data to Excel-friendly format"""
        excel_data = {
            'Metadata': [],
            'Themes': [],
            'Classes': [],
            'Attributes': []
        }

        # Metadata sheet
        metadata = yaml_data.get('model', {})
        excel_data['Metadata'] = [
            {'Key': 'Version', 'Value': yaml_data.get('version', '')},
            {'Key': 'Date', 'Value': yaml_data.get('date', '')},
            {'Key': 'Revision', 'Value': metadata.get('revision', '')},
            {'Key': 'Revision Date', 'Value': metadata.get('revision_date', '')},
        ]

        # Process themes and classes
        for theme in yaml_data.get('themes', []):
            theme_name = theme.get('name', '')

            # Add theme
            excel_data['Themes'].append({
                'Name': theme_name,
                'Description_DE': theme.get('description', {}).get('de', ''),
                'Description_FR': theme.get('description', {}).get('fr', '')
            })

            # Process classes
            for cls in theme.get('classes', []):
                class_name = cls.get('name', '')

                # Add class
                excel_data['Classes'].append({
                    'Theme': theme_name,
                    'Name': class_name,
                    'Abbreviation': cls.get('abrev', ''),
                    'Table': cls.get('table', ''),
                    'Description_DE': cls.get('description', {}).get('de', ''),
                    'Description_FR': cls.get('description', {}).get('fr', '')
                })

                # Process attributes
                for attr in cls.get('attributes', []):
                    excel_data['Attributes'].append({
                        'Theme': theme_name,
                        'Class': class_name,
                        'Name': attr.get('name', ''),
                        'Alias': attr.get('alias', ''),
                        'Type': attr.get('att_type', ''),
                        'Value': attr.get('value', ''),
                        'Description_DE': attr.get('description', {}).get('de', ''),
                        'Description_FR': attr.get('description', {}).get('fr', ''),
                        'Cardinality': attr.get('cardinality', ''),
                        'Mandatory': 'Yes' if attr.get('mandatory') else 'No',
                        'Status': attr.get('status', ''),
                        'Change': attr.get('change', '')
                    })

        return excel_data

    def _write_excel_sheets(self, excel_data: Dict[str, List[Dict]], writer: pd.ExcelWriter):
        """Write data to Excel sheets with formatting"""
        for sheet_name, data in excel_data.items():
            if not data:
                continue

            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

            # Get worksheet for formatting
            worksheet = writer.sheets[sheet_name]

            # Auto-adjust column widths
            for column in worksheet.columns:
                max_length = 0
                column_letter = column[0].column_letter

                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(str(cell.value))
                    except:
                        pass

                adjusted_width = min(max_length + 2, 50)  # Max width of 50
                worksheet.column_dimensions[column_letter].width = adjusted_width

            # Style headers
            if len(df) > 0:
                for cell in worksheet[1]:  # First row (headers)
                    cell.font = writer.book.active.parent._fonts[0].copy(bold=True)
                    cell.fill = writer.book.active.parent._fills[0].copy()


class DataModelImporter:
    """Import Excel back to YAML (for round-trip functionality)"""

    def from_excel(self, excel_file: str, output_yaml: str):
        """Convert Excel file back to YAML datamodel"""
        # Read Excel sheets
        excel_data = pd.read_excel(excel_file, sheet_name=None)

        # Convert back to YAML structure
        yaml_data = self._excel_to_yaml(excel_data)

        # Write YAML file
        with open(output_yaml, 'w', encoding='utf-8') as f:
            yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True)

        logger.info(f"Imported Excel to {output_yaml}")

    def _excel_to_yaml(self, excel_data: Dict[str, pd.DataFrame]) -> Dict[str, Any]:
        """Convert Excel data back to YAML structure"""
        yaml_data = {}

        # Process metadata
        if 'Metadata' in excel_data:
            metadata_df = excel_data['Metadata']
            for _, row in metadata_df.iterrows():
                key = row['Key']
                value = row['Value']

                if key == 'Version':
                    yaml_data['version'] = value
                elif key == 'Date':
                    yaml_data['date'] = value
                elif key in ['Revision', 'Revision Date']:
                    if 'model' not in yaml_data:
                        yaml_data['model'] = {}
                    yaml_data['model'][key.lower().replace(' ', '_')] = value

        # Process themes and classes
        themes = {}

        if 'Classes' in excel_data:
            classes_df = excel_data['Classes']

            for _, row in classes_df.iterrows():
                theme_name = row['Theme']

                if theme_name not in themes:
                    themes[theme_name] = {
                        'name': theme_name,
                        'classes': []
                    }

                class_data = {
                    'name': row['Name'],
                    'abrev': row['Abbreviation'],
                    'table': row['Table'],
                    'description': {
                        'de': row['Description_DE'],
                        'fr': row['Description_FR']
                    },
                    'attributes': []
                }

                themes[theme_name]['classes'].append(class_data)

        # Process attributes
        if 'Attributes' in excel_data:
            attributes_df = excel_data['Attributes']

            # Group attributes by theme and class
            for _, row in attributes_df.iterrows():
                theme_name = row['Theme']
                class_name = row['Class']

                # Find the corresponding class
                theme = themes.get(theme_name)
                if not theme:
                    continue

                target_class = None
                for cls in theme['classes']:
                    if cls['name'] == class_name:
                        target_class = cls
                        break

                if not target_class:
                    continue

                # Add attribute
                attr_data = {
                    'name': row['Name'],
                    'att_type': row['Type'],
                    'description': {
                        'de': row['Description_DE'],
                        'fr': row['Description_FR']
                    },
                    'cardinality': row['Cardinality'],
                    'mandatory': row['Mandatory'].lower() == 'yes'
                }

                # Add optional fields
                if pd.notna(row.get('Alias')):
                    attr_data['alias'] = row['Alias']
                if pd.notna(row.get('Value')):
                    attr_data['value'] = row['Value']
                if pd.notna(row.get('Status')):
                    attr_data['status'] = row['Status']
                if pd.notna(row.get('Change')):
                    attr_data['change'] = row['Change']

                target_class['attributes'].append(attr_data)

        # Convert themes dict to list
        yaml_data['themes'] = list(themes.values())

        return yaml_data