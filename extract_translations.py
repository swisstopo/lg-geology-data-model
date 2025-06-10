import re
import yaml
from pathlib import Path
from typing import Dict, List, Union, Tuple
import jinja2
import json

import re
import yaml
from pathlib import Path
from typing import Dict, List, Union, Tuple
import pandas as pd


def find_files(directories: Union[str, List[str]], extensions: List[str]):
    """Search for files with given extensions in directories."""
    if isinstance(directories, str):
        directories = [directories]

    files = []
    for directory in directories:
        for ext in extensions:
            files.extend(Path(directory).rglob(f"*.{ext}"))
    return files


def extract_jinja_translations(template_path: Path) -> List[Dict[str, str]]:
    """Extract translatable strings from Jinja2 template with file context."""
    with open(template_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    patterns = [
        r'_\("([^"]*)"\)',
        r"_\\('([^']*)'\\)",
        r'gettext\("([^"]*)"\)',
        r"gettext\\('([^']*)'\\)",
        r'{% trans %}(.*?){% endtrans %}',
    ]

    messages = []
    for pattern in patterns:
        matches = re.findall(pattern, source_code, re.DOTALL)
        for match in matches:
            if isinstance(match, tuple):
                match = match[0]
            msg = match.strip()
            if msg:  # Skip empty strings
                print(msg)
                messages.append({
                    "msg_id": f"jinja:{template_path}:{msg}",
                    "source": str(template_path),
                    "text": msg,
                    "type": "jinja",
                    "de": msg,
                    "fr": msg
                })

    return messages


def extract_yaml_translations(yaml_path: Path) -> List[Dict[str, str]]:
    """Extract translations from YAML files with hierarchical paths as identifiers."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing {yaml_path}: {e}")
            return []

    translations = []

    def extract_from_dict(d, current_path: str = ""):
        """Recursively extract translations from nested dictionaries."""
        if isinstance(d, dict):
            for key, value in d.items():
                new_path = f"{current_path}.{key}" if current_path else key

                # Handle translation fields
                if key in ["de", "fr"] and isinstance(value, str):
                    # Find or create entry for this message
                    msg_id = current_path.replace(".", " > ")
                    existing = next((t for t in translations if t["msg_id"] == msg_id), None)
                    if not existing:
                        existing = {
                            "msg_id": msg_id,
                            "source": str(yaml_path),
                            "type": "yaml",
                            "de": "",
                            "fr": ""

                        }
                        translations.append(existing)
                    existing[key] = value.strip()
                else:
                    extract_from_dict(value, new_path)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, dict) and "name" in item:
                    # Use the 'name' field as part of the path if available
                    new_path = f"{current_path}.{item['name']}" if current_path else item['name']
                    extract_from_dict(item, new_path)
                else:
                    extract_from_dict(item, current_path)

    extract_from_dict(data)
    return translations


def extract_all_translations(directories: Union[str, List[str]]):
    """Extract translations from all supported files."""
    all_translations = []

    # Process Jinja2 templates
    for j2_file in find_files(directories, ["j2"]):
        all_translations.extend(extract_jinja_translations(j2_file))

    # Process YAML files
    for yaml_file in find_files(directories, ["yml", "yaml"]):
        all_translations.extend(extract_yaml_translations(yaml_file))

    return all_translations


def save_to_excel(translations: List[Dict[str, str]], output_file: str = "translations.xlsx"):
    """Save translations to Excel file with msg_id, de, fr columns."""
    # Convert to DataFrame
    df = pd.DataFrame(translations)

    # Reorder columns and select only the ones we want
    columns = ["msg_id", "de", "fr", "source", "type"]
    df = df[[col for col in columns if col in df.columns]]

    # Drop duplicates based on msg_id, keeping the first occurrence
    df = df.drop_duplicates(subset=["msg_id"], keep="first")

    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Saved translations to {output_file}")




# Example usage
def main():
    translations_path = 'translations.xlsx'
    translations = extract_all_translations(["templates", "."])  # Add your directories here



    # Print some examples
    print("Sample translations:")
    for i, t in enumerate(translations[:5]):
        print(f"{i + 1}. {t}")


    save_to_excel(translations, output_file=translations_path)









if __name__ == '__main__':
    main()
