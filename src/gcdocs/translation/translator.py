"""
Simplified translation system for gcdocs
Replaces complex babel system with simple CSV-based mapping
"""

import pandas as pd
from typing import Dict, Optional, List
from loguru import logger


class SimpleTranslator:
    """Simplified translator using CSV mapping (replaces complex Translator class)"""

    def __init__(self, translation_df: pd.DataFrame):
        self.translation_df = translation_df
        self.failed_translations: List[str] = []

    def translate(self, geol_code: str, fallback: str, lang: str = "FR") -> str:
        """
        Translate a geological code to the specified language

        Args:
            geol_code: The geological code to translate
            fallback: Fallback text if translation not found
            lang: Target language ("DE" or "FR")

        Returns:
            Translated text or fallback
        """
        if lang not in ("DE", "FR"):
            return fallback

        try:
            # Convert to int for lookup
            code_int = int(geol_code)

            # Look up translation
            translated = self.translation_df.loc[code_int, lang]

            # Clean up French translations (remove "à " prefix)
            if lang == "FR" and isinstance(translated, str) and translated.startswith("à "):
                translated = translated.replace("à ", "")

            return translated

        except (KeyError, ValueError, TypeError) as e:
            # Log failure but don't crash
            self.failed_translations.append(f"{geol_code} ({fallback})")
            logger.debug(f"Translation failed for '{geol_code}': {e}")
            return fallback

    def get_failed_count(self) -> int:
        """Get number of failed translations"""
        return len(self.failed_translations)

    def get_failed_strings(self) -> List[str]:
        """Get list of failed translation strings"""
        return self.failed_translations.copy()

    def clear_failures(self):
        """Clear failed translation tracking"""
        self.failed_translations.clear()


class TranslationManager:
    """Manager for translation operations"""

    @staticmethod
    def create_po_files(translation_df: pd.DataFrame, package_name: str = "gcdocs") -> Dict[str, str]:
        """
        Create PO files for translation (simplified version)
        Returns dict of language -> po_content
        """
        from datetime import datetime

        now = datetime.now()
        tz_str = now.strftime("%Y-%m-%d %H:%M%z")

        po_header_template = f'''# GeoCover Data Model Translations
# Copyright (C) 2024 swisstopo
# This file is distributed under the same license as the {package_name} package.
#
msgid ""
msgstr ""
"Project-Id-Version: {package_name}\\n"
"POT-Creation-Date: {tz_str}\\n"
"PO-Revision-Date: {tz_str}\\n" 
"Last-Translator: geocover <geocover@swisstopo.ch>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=utf-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
'''

        po_files = {}

        for lang in ['de', 'fr']:
            lang_col = lang.upper()
            if lang_col not in translation_df.columns:
                continue

            entries = []
            for geol_code, row in translation_df.iterrows():
                translation = row[lang_col]
                if pd.notna(translation):
                    entries.append(f'\nmsgid "{geol_code}"\nmsgstr "{translation}"')

            po_content = po_header_template + ''.join(entries)
            po_files[lang] = po_content

        # Also create POT template
        pot_entries = []
        for geol_code in translation_df.index:
            pot_entries.append(f'\nmsgid "{geol_code}"\nmsgstr ""')

        pot_content = po_header_template + ''.join(pot_entries)
        po_files['pot'] = pot_content

        return po_files

    @staticmethod
    def write_po_files(po_files: Dict[str, str], output_dir: str = "locale"):
        """Write PO files to disk"""
        import os

        for lang, content in po_files.items():
            if lang == 'pot':
                # Write POT template
                pot_path = os.path.join(output_dir, "datamodel.pot")
                os.makedirs(os.path.dirname(pot_path), exist_ok=True)
                with open(pot_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                logger.info(f"Created POT template: {pot_path}")
            else:
                # Write language-specific PO file
                po_dir = os.path.join(output_dir, lang, "LC_MESSAGES")
                os.makedirs(po_dir, exist_ok=True)
                po_path = os.path.join(po_dir, "datamodel.po")
                with open(po_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                logger.info(f"Created PO file: {po_path}")


def create_translator(translation_df: pd.DataFrame) -> SimpleTranslator:
    """Factory function to create translator"""
    return SimpleTranslator(translation_df)