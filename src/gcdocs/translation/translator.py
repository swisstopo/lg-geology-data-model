"""
Simplified translation system for gcdocs
Replaces complex babel system with simple CSV-based mapping
"""

import pandas as pd
from typing import Dict, Optional, List
from loguru import logger
import pandas as pd
import logging
import threading
import sys

SUPPORTED_LANGUAGES = ("DE", "FR", "IT", "EN")


class SimpleTranslator:
    """Simplified translator using CSV mapping (replaces complex Translator class)"""

    def __init__(self, translation_df: pd.DataFrame):
        self.translation_df = translation_df
        self.failed_translations: List[str] = []

    def __str__(self):
        return f"<SimpleTranslator: {len(self.translation_df)} translations, lang: {self.translation_df.columns}>"

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
        if lang not in SUPPORTED_LANGUAGES:
            return fallback

        try:
            # Convert to int for lookup
            code_int = int(geol_code)

            # Look up translation
            translated = self.translation_df.loc[code_int, lang]

            # Clean up French translations (remove "à " prefix)
            if (
                lang == "FR"
                and isinstance(translated, str)
                and translated.startswith("à ")
            ):
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
    def create_po_files(
        translation_df: pd.DataFrame, package_name: str = "gcdocs"
    ) -> Dict[str, str]:
        """
        Create PO files for translation (simplified version)
        Returns dict of language -> po_content
        """
        from datetime import datetime

        now = datetime.now()
        tz_str = now.strftime("%Y-%m-%d %H:%M%z")

        po_header_template = f"""# GeoCover Data Model Translations
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
"""

        po_files = {}

        for lang in SUPPORTED_LANGUAGES:
            lang_col = lang.upper()
            if lang_col not in translation_df.columns:
                continue

            entries = []
            for geol_code, row in translation_df.iterrows():
                translation = row[lang_col]
                if pd.notna(translation):
                    entries.append(f'\nmsgid "{geol_code}"\nmsgstr "{translation}"')

            po_content = po_header_template + "".join(entries)
            po_files[lang] = po_content

        # Also create POT template
        pot_entries = []
        for geol_code in translation_df.index:
            pot_entries.append(f'\nmsgid "{geol_code}"\nmsgstr ""')

        pot_content = po_header_template + "".join(pot_entries)
        po_files["pot"] = pot_content

        return po_files

    @staticmethod
    def write_po_files(po_files: Dict[str, str], output_dir: str = "locale"):
        """Write PO files to disk"""
        import os

        for lang, content in po_files.items():
            if lang == "pot":
                # Write POT template
                pot_path = os.path.join(output_dir, "datamodel.pot")
                os.makedirs(os.path.dirname(pot_path), exist_ok=True)
                with open(pot_path, "w", encoding="utf-8") as f:
                    f.write(content)
                logger.info(f"Created POT template: {pot_path}")
            else:
                # Write language-specific PO file
                po_dir = os.path.join(output_dir, lang, "LC_MESSAGES")
                os.makedirs(po_dir, exist_ok=True)
                po_path = os.path.join(po_dir, "datamodel.po")
                with open(po_path, "w", encoding="utf-8") as f:
                    f.write(content)
                logger.info(f"Created PO file: {po_path}")


class Translator:
    def __init__(self, df_trad):
        """
        Initialize translator with geological codes dataframe.

        Args:
            df_trad (pd.DataFrame): DataFrame with columns ['GeolCodeInt', 'DE', 'FR']
                                   or similar structure for translations
        """
        self.failed_translations = 0
        self.failed_strings: List[str] = []
        self._lock = threading.Lock()
        self.df_trad = df_trad

        # Create lookup dictionaries for faster access
        self._create_lookup_dicts()

    def __repr__(self):
        return f"<Translator: {len(self.df_trad)} translations, langs: {self.df_trad.columns}>"

    def get_failed_count(self) -> int:
        """Get number of failed translations"""
        return len(self.failed_strings)

    def get_failed_strings(self) -> List[str]:
        """Get list of failed translation strings"""
        return self.failed_strings.copy()

    def clear_failures(self):
        """Clear failed translation tracking"""
        self.failed_strings.clear()

    def _create_lookup_dicts(self):
        """Create lookup dictionaries from the translation dataframe."""
        self.translations = {}

        logger.debug(f"Translation dataframe:  {len(self.df_trad)}")

        if self.df_trad is not None and not self.df_trad.empty:
            # Check if GeolCodeInt is the index, otherwise look for it as a column
            if self.df_trad.index.name == "GeolCodeInt":
                # Index is already set to GeolCodeInt - perfect!
                for geol_code_int, row in self.df_trad.iterrows():
                    code = str(geol_code_int)
                    self.translations[code] = {
                        "DE": row.get("DE") if pd.notna(row.get("DE", None)) else None,
                        "FR": row.get("FR") if pd.notna(row.get("FR", None)) else None,
                        "IT": row.get("IT") if pd.notna(row.get("IT", None)) else None,
                        "EN": row.get("EN") if pd.notna(row.get("EN", None)) else None,
                    }
            else:
                # Fallback to column-based approach
                if "GeolCodeInt" in self.df_trad.columns:
                    for _, row in self.df_trad.iterrows():
                        code = str(row["GeolCodeInt"])
                        self.translations[code] = {
                            "DE": row.get("DE")
                            if pd.notna(row.get("DE", None))
                            else None,
                            "FR": row.get("FR")
                            if pd.notna(row.get("FR", None))
                            else None,
                            "IT": row.get("IT")
                            if pd.notna(row.get("IT", None))
                            else None,
                            "EN": row.get("EN")
                            if pd.notna(row.get("EN", None))
                            else None,
                        }
                else:
                    logger.warning(
                        "Neither GeolCodeInt index nor column found in dataframe"
                    )

        logger.debug(f"Lookup dict with {len(self.translations)} translation entries")

    # TODO: No translation found for code 'Revision %(name)s' in IT or FR
    def translate(self, text, lang="FR", **kwargs):
        """
        Public method to translate geological codes or formatted strings.

        Args:
            text: The geological code or string to translate
            lang: Target language ("FR" or "DE")
            **kwargs: Named parameters for string formatting (e.g., name=value)

        Returns:
            str: Translated and formatted text, or original if translation fails

        Examples:
            translate("12345", "FR")  # Simple code translation
            translate("Revision %(name)s", "FR", name="2024-v1")  # Formatted string
        """
        translated_text, err = self._translate(text, lang)

        if err:
            with self._lock:
                self.failed_strings.append(str(text))

        # Apply formatting if kwargs provided
        if kwargs:
            try:
                translated_text = translated_text % kwargs
            except (KeyError, ValueError, TypeError) as e:
                logger.warning(f"Failed to format '{translated_text}' with {kwargs}: {e}")
                # Fallback: try to format original text
                try:
                    translated_text = str(text) % kwargs
                except Exception:
                    pass  # Keep translated_text as-is

        return translated_text

    def _translate(self, text, lang):
        """
        Internal translation method with intelligent fallback logic.

        Handles both:
        - Simple geological codes (e.g., "12345")
        - Template strings with placeholders (e.g., "Revision %(name)s")

        Priority order:
        1. Requested language (FR or DE)
        2. German (DE) if French was requested but not available
        3. French (FR) if German was requested but not available
        4. Original text

        Args:
            text: The geological code or string to translate
            lang: Requested language ("FR" or "DE")

        Returns:
            tuple: (translated_message, error_occurred)
        """
        msg = str(text)
        err = False

        # Handle special case for code "0"
        if str(text) == "0":
            return ("–", False)

        # Only process supported languages
        if lang not in SUPPORTED_LANGUAGES:
            logger.error(f"Unknown lang: {lang}")
            return (msg, False)

        try:
            text_str = str(text)

            # Try primary language first
            primary_msg = self._get_translation(text_str, lang)

            if primary_msg is not None:  # TODO: using `and primary_msg != text_str`
                logger.debug(f"Translating into {lang}: {text_str} -> {primary_msg}")
                return (self._clean_message(primary_msg), False)

            # Try fallback language
            fallback_lang = "DE" if lang in ("FR", "EN") else "FR"
            fallback_msg = self._get_translation(text_str, fallback_lang)

            if fallback_msg is not None:
                logger.warning(
                    f"Using {fallback_lang} fallback: '{text}' -> '{fallback_msg}' "
                    f"(requested: {lang})"
                )
                return (self._clean_message(fallback_msg), False)

            # No translation found in either language
            err = True
            logger.error(
                f"No translation found for '{text}' in {lang} or {fallback_lang}"
            )

        except Exception as e:
            err = True
            logger.error(f"Error translating '{text}': {e}")

        return (msg, err)


    def _get_translation(self, geol_code_str, lang):
        """
        Get translation for a specific code and language.

        Args:
            geol_code_str: String representation of geological code
            lang: Language code ("DE" or "FR")

        Returns:
            str or None: Translation if found, None otherwise
        """
        if geol_code_str in self.translations:
            translation = self.translations[geol_code_str].get(lang)
            if translation and str(translation).strip():
                return translation
        return None

    def _clean_message(self, message):
        """
        Clean and format the translated message.

        Args:
            message: Raw translation message

        Returns:
            str: Cleaned message
        """
        if message is None:
            return ""

        # Convert to string and strip whitespace
        cleaned = str(message).strip()

        # Remove any extra spaces
        cleaned = " ".join(cleaned.split())

        return cleaned

    def get_translation_stats(self):
        """
        Get statistics about translation failures.

        Returns:
            dict: Statistics including failed count and failed strings
        """
        with self._lock:
            return {
                "failed_translations": len(self.failed_strings),
                "failed_strings": self.failed_strings.copy(),
                "total_codes_loaded": len(self.translations),
            }

    def reset_stats(self):
        """Reset translation failure statistics."""
        with self._lock:
            # self.failed_translations = 0
            self.failed_strings = []


def create_simple_translator(translation_df: pd.DataFrame) -> SimpleTranslator:
    """Factory function to create translator"""
    return SimpleTranslator(translation_df)


def create_translator(translation_df: pd.DataFrame) -> SimpleTranslator:
    """Factory function to create translator"""
    logger.debug(len(translation_df))
    return Translator(translation_df)


def create_test_data():
    """Create test DataFrame with sample geological codes."""
    data = {
        "10002001": {"DE": "historisch", "FR": "historique"},
        "10002002": {"DE": "prähistorisch", "FR": "préhistorique"},
        "10003001": {"DE": "Neuzeit", "FR": "époque moderne"},
        "10003002": {"DE": "Mittelalter", "FR": None},  # Missing French translation
        "10003003": {"DE": None, "FR": "époque romaine"},  # Missing German translation
    }

    df = pd.DataFrame.from_dict(data, orient="index")
    df.index.name = "GeolCodeInt"  # Rename the index
    df.index = df.index.astype(str)  # Convert index to string
    print("Test DataFrame:")
    print(df)
    print()
    return df


def run_tests():
    """Run comprehensive tests of the Translator class."""

    # Create test data
    df_trad = create_test_data()
    translator = Translator(df_trad)

    print("=== TRANSLATOR TESTS ===\n")

    # Test 1: Normal translations (both languages available)
    print("1. Normal translations:")
    print(f"  FR 10002001: '{translator.translate('10002001', 'FR')}'")
    print(f"  DE 10002001: '{translator.translate('10002001', 'DE')}'")
    print()

    # Test 2: French fallback to German (FR missing)
    print("2. French fallback to German:")
    print(f"  FR 10003002: '{translator.translate('10003002', 'FR')}'")
    print()

    # Test 3: German fallback to French (DE missing)
    print("3. German fallback to French:")
    print(f"  DE 10003003: '{translator.translate('10003003', 'DE')}'")
    print()

    # Test 4: Complete failure (code doesn't exist)
    print("4. Complete failure (unknown code):")
    print(f"  FR 99999999: '{translator.translate('99999999', 'FR')}'")
    print()

    # Test 5: Special case (code "0")
    print("5. Special case (code '0'):")
    print(f"  FR 0: '{translator.translate('0', 'FR')}'")
    print()

    # Test 6: Unsupported language
    print("6. Unsupported language:")
    print(f"  EN 10002001: '{translator.translate('10002001', 'EN')}'")
    print()

    # Test 7: Unsupported language
    print("7. Hardcoded values (unbekannt):")
    print(f"  DE 999997: '{translator.translate('999997', 'DE')}'")
    print()

    # Test 8: Unsupported language
    print("8. Hardcoded values (non applicable):")
    print(f"  FR 999998: '{translator.translate('999998', 'FR')}'")
    print()

    # Test 7: Check error statistics
    print("7. Error statistics:")
    print(f"  Failed translations: {translator.get_failed_count()}")
    print(f"  Failed strings: {translator.get_failed_strings()}")
    print()


if __name__ == "__main__":
    run_tests()
