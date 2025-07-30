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

import gettext
from pathlib import Path

from loguru import logger


def load_existing_translations(locale_dir="locale", domain="app"):
    """Load existing translations from locale directory"""
    translations = {}

    # Find all available languages
    for lang_dir in Path(locale_dir).iterdir():
        if not lang_dir.is_dir():
            continue

        lang = lang_dir.name
        try:
            # Load the MO file
            mo_path = lang_dir / "LC_MESSAGES" / f"{domain}.mo"
            if mo_path.exists():
                with open(mo_path, "rb") as f:
                    translations[lang] = gettext.GNUTranslations(f)
        except Exception as e:
            logger.error(f"Error loading {mo_path}: {e}")

    return translations


def find_files(
    paths: Union[str, Path, List[Union[str, Path]]], extensions: List[str]
) -> List[Path]:
    """
    Find files with given extensions from directories or file paths.

    Args:
        paths: Can be:
            - A single directory path (str or Path)
            - A single file path (str or Path)
            - A list of mixed directories and file paths
        extensions: List of file extensions to include (e.g., ['j2', 'yaml'])

    Returns:
        List of Path objects matching the extensions
    """
    if not isinstance(paths, list):
        paths = [paths]

    collected_files = []

    for path in paths:
        path = Path(path) if isinstance(path, str) else path

        if path.is_file():
            # If it's a file, check extension and add if matching
            if path.suffix.lstrip(".") in extensions:
                collected_files.append(path)
        elif path.is_dir():
            # If it's a directory, search recursively for matching extensions
            for ext in extensions:
                collected_files.extend(path.rglob(f"*.{ext}"))
        else:
            logger.warning(f"Warning: Path does not exist - {path}")

    # Remove duplicates while preserving order
    seen = set()
    return [f for f in collected_files if not (f in seen or seen.add(f))]


def extract_jinja_translations(template_path: Path) -> List[Dict[str, str]]:
    """Extract translatable strings from Jinja2 template with line numbers."""
    with open(template_path, "r", encoding="utf-8") as f:
        source_code = f.readlines()  # Read as lines to get line numbers

    patterns = [
        r'_\("([^"]*)"\)',
        r"_\\('([^']*)'\\)",
        r'gettext\("([^"]*)"\)',
        r"gettext\\('([^']*)'\\)",
        r"{% trans %}(.*?){% endtrans %}",
    ]

    messages = []

    # Convert back to single string for regex matching
    full_text = "".join(source_code)

    for pattern in patterns:
        # Find all matches in the full text
        matches = re.finditer(pattern, full_text, re.DOTALL)

        for match in matches:
            if match.groups():
                msg = match.group(1).strip()
                if msg:
                    # Calculate line number
                    line_no = full_text[: match.start()].count("\n") + 1
                    messages.append(
                        {
                            "msg_id": f"{msg}",
                            "source": f"jinja:{template_path}:{line_no}",
                            "type": "jinja",
                            "de": "",
                            "fr": "",
                        }
                    )

    return messages


def extract_yaml_translations(yaml_path: Path) -> List[Dict[str, str]]:
    """Extract translations from YAML files with hierarchical paths as identifiers."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logger.error(f"Error parsing {yaml_path}: {e}")
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
                    existing = next(
                        (t for t in translations if t["msg_id"] == msg_id), None
                    )
                    if not existing:
                        existing = {
                            "msg_id": msg_id,
                            "source": str(yaml_path),
                            "type": "yaml",
                            "de": "",
                            "fr": "",
                        }
                        translations.append(existing)
                    existing[key] = value.strip()
                else:
                    extract_from_dict(value, new_path)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, dict) and "name" in item:
                    # Use the 'name' field as part of the path if available
                    new_path = (
                        f"{current_path}.{item['name']}"
                        if current_path
                        else item["name"]
                    )
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
    # TODO
    for yaml_file in find_files(directories, ["yml", "yaml"]):  #
        all_translations.extend(extract_yaml_translations(yaml_file))

    return all_translations


def apply_existing_translations(df, existing_translations):
    """Fill in existing translations from .mo files"""
    # Create columns for each language if they don't exist
    for lang in existing_translations.keys():
        if lang not in df.columns:
            df[lang] = ""

    # For each row, try to find existing translations
    for index, row in df.iterrows():
        msg_id = row["msg_id"]
        for lang, trans in existing_translations.items():
            # Only fill if the target column is empty
            if pd.isna(row[lang]) or row[lang] == "":
                # Get translation (returns original if not found)
                translated = trans.gettext(msg_id)

                if translated != msg_id:  # Only update if translation exists
                    df.at[index, lang] = translated

    return df


def save_to_excel(
    translations: List[Dict[str, str]], output_file: str = "translations.xlsx"
):
    """Save translations to Excel file with msg_id, de, fr columns."""
    # Convert to DataFrame
    df = pd.DataFrame(translations)

    # Reorder columns and select only the ones we want
    columns = ["msg_id", "de", "fr", "source", "type"]
    df = df[[col for col in columns if col in df.columns]]

    # Drop duplicates based on msg_id, keeping the first occurrence
    df = df.drop_duplicates(subset=["msg_id"], keep="first")

    # Load existing translations and apply them
    existing_translations = load_existing_translations()
    df = apply_existing_translations(df, existing_translations)

    # Save to Excel
    df.to_excel(output_file, index=False)
    logger.info(f"Saved translations to {output_file}")


# Example usage
def main():
    translations_path = "translations.xlsx"
    EXTRACT_FILES_DIR = ["templates", "datamodel.yaml"]

    logger.info(f"Extracting translation from: {EXTRACT_FILES_DIR}")
    translations = extract_all_translations(EXTRACT_FILES_DIR)

    # Print some examples
    logger.debug("Sample translations:")
    for i, t in enumerate(translations[:5]):
        logger.debug(f"{i + 1}. {t}")

    save_to_excel(translations, output_file=translations_path)


if __name__ == "__main__":
    main()
