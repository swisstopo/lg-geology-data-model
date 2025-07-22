import pandas as pd
import logging
import threading
import sys

from loguru import logger


class Translator:
    def __init__(self, df_trad):
        """
        Initialize translator with geological codes dataframe.

        Args:
            df_trad (pd.DataFrame): DataFrame with columns ['ID', 'German', 'French']
                                   or similar structure for translations
        """
        self.failed_translations = 0
        self.failed_strings = []
        self._lock = threading.Lock()
        self.df_trad = df_trad

        # Create lookup dictionaries for faster access
        self._create_lookup_dicts()

        # sys.exit()

    def _create_lookup_dicts(self):
        """Create lookup dictionaries from the translation dataframe."""
        self.translations = {}

        if self.df_trad is not None and not self.df_trad.empty:
            # Check if GeolCodeInt is the index, otherwise look for it as a column
            if self.df_trad.index.name == "GeolCodeInt":
                # Index is already set to GeolCodeInt - perfect!
                for geol_code_int, row in self.df_trad.iterrows():
                    code = str(geol_code_int)
                    self.translations[code] = {
                        "DE": row.get("DE") if pd.notna(row.get("DE", None)) else None,
                        "FR": row.get("FR") if pd.notna(row.get("FR", None)) else None,
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
                        }
                else:
                    logger.warning(
                        "Neither GeolCodeInt index nor column found in dataframe"
                    )

        logger.debug(self.translations)

        logger.info(f"Loaded {len(self.translations)} translation entries")

    def translate(self, geol_code, lang="FR"):
        """
        Public method to translate geological codes with error tracking.

        Args:
            geol_code: The geological code to translate
            lang: Target language ("FR" or "DE")

        Returns:
            str: Translated text or original code if translation fails
        """
        translated_text, err = self._translate(geol_code, lang)

        if err:
            with self._lock:
                self.failed_translations += 1
                self.failed_strings.append(str(geol_code))  # Fixed: was 'text'

        return translated_text

    def _translate(self, geol_code, lang):
        """
        Internal translation method with intelligent fallback logic.

        Priority order:
        1. Requested language (FR or DE)
        2. German (DE) if French was requested but not available
        3. French (FR) if German was requested but not available
        4. Original geological code

        Args:
            geol_code: The geological code to translate
            lang: Requested language ("FR" or "DE")

        Returns:
            tuple: (translated_message, error_occurred)
        """
        msg = str(geol_code)
        err = False

        # Handle special case for code "0"
        if str(geol_code) == "0":
            return ("–", False)

        # Only process supported languages
        if lang not in ("DE", "FR"):
            logger.debug(f"Unknown lang: {lang}")
            return (msg, False)

        try:
            geol_code_str = str(geol_code)
            logger.debug(f"Translating: {geol_code_str}")

            # Try primary language first
            primary_msg = self._get_translation(geol_code_str, lang)

            if primary_msg is not None and primary_msg != geol_code_str:
                return (self._clean_message(primary_msg), False)

            # Try fallback language
            fallback_lang = "DE" if lang == "FR" else "FR"
            fallback_msg = self._get_translation(geol_code_str, fallback_lang)

            if fallback_msg is not None:
                logger.warning(
                    f"Using {fallback_lang} fallback '{fallback_msg}' for code '{geol_code}' (requested: {lang})"
                )
                return (self._clean_message(fallback_msg), False)

            # No translation found in either language
            err = True
            logger.debug(
                f"No translation found for code '{geol_code}' in {lang} or {fallback_lang}"
            )

        except Exception as e:
            err = True
            logger.error(f"Error translating code '{geol_code}': {e}")

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
                "failed_translations": self.failed_translations,
                "failed_strings": self.failed_strings.copy(),
                "total_codes_loaded": len(self.translations),
            }

    def reset_stats(self):
        """Reset translation failure statistics."""
        with self._lock:
            self.failed_translations = 0
            self.failed_strings = []


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
    print(f"  FR 10002001: '{translator.translate('10002001', 'fallback_text', 'FR')}'")
    print(f"  DE 10002001: '{translator.translate('10002001', 'fallback_text', 'DE')}'")
    print()

    # Test 2: French fallback to German (FR missing)
    print("2. French fallback to German:")
    print(f"  FR 10003002: '{translator.translate('10003002', 'fallback_text', 'FR')}'")
    print()

    # Test 3: German fallback to French (DE missing)
    print("3. German fallback to French:")
    print(f"  DE 10003003: '{translator.translate('10003003', 'fallback_text', 'DE')}'")
    print()

    # Test 4: Complete failure (code doesn't exist)
    print("4. Complete failure (unknown code):")
    print(f"  FR 99999999: '{translator.translate('99999999', 'fallback_text', 'FR')}'")
    print()

    # Test 5: Special case (code "0")
    print("5. Special case (code '0'):")
    print(f"  FR 0: '{translator.translate('0', 'fallback_text', 'FR')}'")
    print()

    # Test 6: Unsupported language
    print("6. Unsupported language:")
    print(f"  EN 10002001: '{translator.translate('10002001', 'fallback_text', 'EN')}'")
    print()

    # Test 7: Check error statistics
    print("7. Error statistics:")
    print(f"  Failed translations: {translator.get_failed_count()}")
    print(f"  Failed strings: {translator.get_failed_strings()}")
    print()


if __name__ == "__main__":
    run_tests()
