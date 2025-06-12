import pandas as pd
import logging
import threading

from loguru import logger


class Translator:
    def __init__(self, df_trad):
        self.failed_translations = 0
        self.failed_strings = []
        self._lock = threading.Lock()  # Ensures thread safety
        self.df_trad = df_trad

    def translate(self, geol_code, text, lang="FR"):
        """
        Public method to translate with error tracking.

        Args:
            geol_code: The geological code to translate
            text: Fallback text if translation fails
            lang: Target language ("FR" or "DE")

        Returns:
            str: Translated text or fallback
        """
        translated_text, err = self._translate(geol_code, text, lang)

        if err:
            with self._lock:
                self.failed_translations += 1
                self.failed_strings.append(text)

        return translated_text

    def _translate(self, geol_code, fallback, lang):
        """
        Internal translation method with intelligent fallback logic.

        Priority order:
        1. Requested language (FR or DE)
        2. German (DE) if French was requested but not available
        3. French (FR) if German was requested but not available
        4. Original fallback message

        Args:
            geol_code: The geological code to translate
            fallback: Default message if no translation found
            lang: Requested language ("FR" or "DE")

        Returns:
            tuple: (translated_message, error_occurred)
        """
        msg = fallback
        err = False

        # Handle special case for code "0"
        if str(geol_code) == "0":
            return ("–", False)

        # Only process supported languages
        if lang not in ("DE", "FR"):
            return (msg, False)

        try:
            geol_code_str = str(geol_code)

            # Try primary language first
            primary_msg = self._get_translation(geol_code_str, lang)
            if primary_msg is not None:
                return (self._clean_message(primary_msg), False)

            # Try fallback language (German if French requested, French if German requested)
            fallback_lang = "DE" if lang == "FR" else "FR"
            fallback_msg = self._get_translation(geol_code_str, fallback_lang)
            if fallback_msg is not None:
                logger.warning(
                    f"Using {fallback_lang} fallback for geol_code '{geol_code}' (requested: {lang})"
                )
                return (self._clean_message(fallback_msg), False)

            # No translation found in either language
            err = True
            logger.error(
                f"No translation found for geol_code '{geol_code}' in {lang} or {fallback_lang}"
            )

        except Exception as e:
            err = True
            logger.error(f"Error translating geol_code '{geol_code}': {e}")

        return (msg, err)

    def _get_translation(self, geol_code_str, language):
        """
        Helper method to get translation for a specific language.

        Args:
            geol_code_str: Geological code as string
            language: Language code ("FR" or "DE")

        Returns:
            str or None: Translation if found and valid, None otherwise
        """
        try:
            value = self.df_trad.loc[geol_code_str, language]

            # Handle Series (multiple matches)
            if isinstance(value, pd.Series):
                value = value.iloc[0]

            # Check if translation is valid (not empty, not NaN, not just whitespace)
            if pd.isna(value) or str(value).strip() == "":
                return None

            return str(value)

        except KeyError:
            return None

    def _clean_message(self, message):
        """
        Clean up translation message by removing unwanted prefixes.

        Args:
            message: Raw translation message

        Returns:
            str: Cleaned message
        """
        if isinstance(message, str) and message.startswith("à "):
            return message.replace("à ", "")
        return message

    def get_failed_count(self):
        """Get the number of failed translations."""
        return self.failed_translations

    def get_failed_strings(self):
        """Get the list of strings that failed to translate."""
        return self.failed_strings

    def reset_failed_stats(self):
        """Reset the failed translation statistics."""
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
