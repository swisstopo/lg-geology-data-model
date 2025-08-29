"""
Configuration and data loading for gcdocs
Replaces global variables from original datamodel.py
"""

import json
import os
import pandas as pd
from pathlib import Path
from typing import Dict, Any, Optional
from loguru import logger


class GeoDataConfig:
    """Configuration class that loads and manages geological data"""

    def __init__(self, input_dir: str = "exports"):
        self.input_dir = Path(input_dir)
        self._domains: Optional[Dict[str, Any]] = None
        self._subtypes: Optional[Dict[str, Any]] = None
        self._sde_schema: Optional[Dict[str, Any]] = None
        self._translation_df: Optional[pd.DataFrame] = None
        self._tables_dict: Optional[Dict[str, Any]] = None

    @property
    def domains(self) -> Dict[str, Any]:
        """Load coded domains (replaces global 'domains')"""
        if self._domains is None:
            domains_file = self.input_dir / "coded_domains.json"
            if not domains_file.exists():
                raise FileNotFoundError(f"Domains file not found: {domains_file}")

            with open(domains_file, "r") as f:
                self._domains = json.load(f)
            logger.info(f"Loaded domains from {domains_file}")
        return self._domains

    @property
    def subtypes(self) -> Dict[str, Any]:
        """Load subtypes (replaces global 'subtypes')"""
        if self._subtypes is None:
            subtypes_file = self.input_dir / "subtypes_dict.json"
            if not subtypes_file.exists():
                raise FileNotFoundError(f"Subtypes file not found: {subtypes_file}")

            with open(subtypes_file, "r") as f:
                self._subtypes = json.load(f)
            logger.info(f"Loaded subtypes from {subtypes_file}")
        return self._subtypes

    @property
    def sde_schema(self) -> Dict[str, Any]:
        """Load SDE schema (replaces global 'sde_schema')"""
        if self._sde_schema is None:
            schema_file = self.input_dir / "gcoverp_export_simple.json"
            if not schema_file.exists():
                raise FileNotFoundError(f"Schema file not found: {schema_file}")

            with open(schema_file, "r") as f:
                self._sde_schema = json.load(f)
            logger.info(f"Loaded SDE schema from {schema_file}")
        return self._sde_schema

    @property
    def tables_dict(self) -> Dict[str, Any]:
        """Combined tables dictionary (replaces global 'tables_dict')"""
        if self._tables_dict is None:
            schema = self.sde_schema
            featclasses_dict = schema.get("featclasses", {})
            tables_ = schema.get("tables", {})
            self._tables_dict = featclasses_dict | tables_
        return self._tables_dict

    @property
    def translation_df(self) -> pd.DataFrame:
        """Load translation DataFrame from multiple sources (replaces global 'df')"""
        if self._translation_df is None:
            self._translation_df = self._load_merged_translations()
        return self._translation_df

    def _load_merged_translations(self) -> pd.DataFrame:
        """Load and merge translation data from multiple sources"""
        try:
            dataframes = []

            # 1. Load CSV translation file (legacy/main source)
            csv_file = self._find_file("GeolCodeText_Trad_230317.csv")
            if csv_file:
                df_csv = pd.read_csv(csv_file, sep=";")
                df_csv["GeolCodeInt"] = df_csv["GeolCodeInt"].astype("string")
                dataframes.append(df_csv)
                logger.debug(f"Loaded CSV translations: {len(df_csv)} entries")

            # 2. Load new Excel translations (if available)
            excel_file = self._find_file("GeolCodeText_Trad_2025.xlsx")
            if excel_file:
                df_excel = pd.read_excel(excel_file, sheet_name="Tabelle1")
                df_excel["GeolCodeInt"] = df_excel["GeolCodeInt"].astype("string")
                dataframes.append(df_excel)
                logger.debug(f"Loaded Excel translations: {len(df_excel)} entries")

            # 3. Load JSON coded domains (fallback German -> French)
            json_file = self._find_file("all_codes_dict.json")
            if json_file:
                with open(json_file, "r", encoding="utf-8") as f:
                    code_dict = json.load(f)

                df_json = pd.DataFrame({
                    "GeolCodeInt": list(code_dict.keys()),
                    "DE": list(code_dict.values()),
                    "FR": list(code_dict.values())  # Use German as fallback for French
                })
                df_json["GeolCodeInt"] = df_json["GeolCodeInt"].astype("string")
                dataframes.append(df_json)
                logger.debug(f"Loaded JSON translations: {len(df_json)} entries")

            # 4. Load custom chronology translations (if available)
            chrono_file = self._find_file("geolcode_chrono.csv")
            if chrono_file:
                df_chrono = pd.read_csv(chrono_file)
                df_chrono["GeolCodeInt"] = df_chrono["GeolCodeInt"].astype("string")
                dataframes.append(df_chrono)
                logger.debug(f"Loaded chrono translations: {len(df_chrono)} entries")

            # 5. Load application UI translations (if available)
            app_translations = self._find_file("translations.xlsx")
            if app_translations:
                df_app = pd.read_excel(app_translations, usecols=["msg_id", "de", "fr"])
                df_app.columns = df_app.columns.str.upper()
                df_app.rename(columns={"MSG_ID": "GeolCodeInt"}, inplace=True)
                df_app["GeolCodeInt"] = df_app["GeolCodeInt"].astype("string")
                dataframes.append(df_app)
                logger.debug(f"Loaded app translations: {len(df_app)} entries")

            # 6. Add special hardcoded values
            special_codes = pd.DataFrame([
                {"GeolCodeInt": "999997", "DE": "unbekannt", "FR": "inconnu"},
                {"GeolCodeInt": "999998", "DE": "nicht anwendbar", "FR": "pas applicable"},
            ])
            special_codes["GeolCodeInt"] = special_codes["GeolCodeInt"].astype("string")
            dataframes.append(special_codes)

            if not dataframes:
                logger.warning("No translation files found, creating empty DataFrame")
                return pd.DataFrame(columns=["DE", "FR"]).astype("string")

            # Merge all dataframes
            merged_df = pd.concat(dataframes, ignore_index=True)

            # Clean and process
            translation_df = self._clean_translation_data(merged_df)

            logger.info(f"Loaded merged translations: {len(translation_df)} total entries")
            return translation_df

        except Exception as e:
            logger.error(f"Failed to load translation data: {e}")
            # Return minimal DataFrame with special codes
            return pd.DataFrame([
                {"GeolCodeInt": "999997", "DE": "unbekannt", "FR": "inconnu"},
                {"GeolCodeInt": "999998", "DE": "nicht anwendbar", "FR": "pas applicable"},
            ]).set_index("GeolCodeInt")

    def _find_file(self, filename: str) -> Optional[Path]:
        """Find a file in the input directory or package data"""
        # Try input directory first
        file_path = self.input_dir / filename
        if file_path.exists():
            return file_path

        # Try package data directory
        try:
            from importlib import resources
            with resources.path("gcdocs.data", filename) as data_path:
                if data_path.exists():
                    return data_path
        except (ImportError, FileNotFoundError):
            pass

        # Try current directory
        current_path = Path(filename)
        if current_path.exists():
            return current_path

        logger.debug(f"Translation file not found: {filename}")
        return None

    def _clean_translation_data(self, merged_df: pd.DataFrame) -> pd.DataFrame:
        """Clean and process the merged translation DataFrame"""
        # Ensure required columns exist
        required_cols = ["GeolCodeInt", "DE", "FR"]
        for col in required_cols:
            if col not in merged_df.columns:
                merged_df[col] = ""

        # Clean the data
        cleaned_df = (
            merged_df[required_cols]  # Select only required columns
            .drop_duplicates(subset=["GeolCodeInt"], keep="last")  # Remove duplicates, keep latest
            .assign(
                # Convert all to string and clean
                GeolCodeInt=lambda x: x["GeolCodeInt"].astype("string"),
                DE=lambda x: x["DE"].astype("string").replace(["0", "nan", "None"], "-"),
                FR=lambda x: x["FR"].astype("string").replace(["0", "nan", "None"], "-")
            )
            .query("GeolCodeInt != '' and GeolCodeInt != 'nan'")  # Remove empty codes
            .sort_values("GeolCodeInt")
            .set_index("GeolCodeInt")
        )

        return cleaned_df

    def _clean_translation_data(self, merged_df: pd.DataFrame) -> pd.DataFrame:
        """Clean and process the merged translation DataFrame"""
        # Ensure required columns exist
        required_cols = ["GeolCodeInt", "DE", "FR"]
        for col in required_cols:
            if col not in merged_df.columns:
                merged_df[col] = ""

        # Clean the data
        cleaned_df = (
            merged_df[required_cols]  # Select only required columns
            .drop_duplicates(subset=["GeolCodeInt"], keep="last")  # Remove duplicates, keep latest
            .assign(
                # Convert all to string and clean
                GeolCodeInt=lambda x: x["GeolCodeInt"].astype("string"),
                DE=lambda x: x["DE"].astype("string").replace(["0", "nan", "None"], "-"),
                FR=lambda x: x["FR"].astype("string").replace(["0", "nan", "None"], "-")
            )
            .query("GeolCodeInt != '' and GeolCodeInt != 'nan'")  # Remove empty codes
            .sort_values("GeolCodeInt")
            .set_index("GeolCodeInt")
        )

        return cleaned_df

    def save_merged_translations(self, output_path: Optional[str] = None) -> Path:
        """Save the merged translation DataFrame to Excel"""
        if output_path is None:
            output_path = self.input_dir / "all_translations_merged.xlsx"
        else:
            output_path = Path(output_path)

        translation_df = self.translation_df
        translation_df.to_excel(output_path, index=True, engine="openpyxl")
        logger.info(f"Saved merged translations to {output_path}")
        return output_path

    def get_translation_stats(self) -> Dict[str, Any]:
        """Get statistics about the loaded translations"""
        df = self.translation_df

        return {
            "total_entries": len(df),
            "german_translations": len(df[df["DE"] != "-"]),
            "french_translations": len(df[df["FR"] != "-"]),
            "missing_german": len(df[df["DE"] == "-"]),
            "missing_french": len(df[df["FR"] == "-"]),
            "complete_entries": len(df[(df["DE"] != "-") & (df["FR"] != "-")]),
        }

    def add_custom_translations(self, custom_translations: Dict[str, Dict[str, str]]):
        """Add custom translations to the existing DataFrame

        Args:
            custom_translations: Dict like {"123": {"DE": "German text", "FR": "French text"}}
        """
        if not custom_translations:
            return

        custom_df = pd.DataFrame.from_dict(custom_translations, orient='index')
        custom_df.index.name = 'GeolCodeInt'
        custom_df.index = custom_df.index.astype('string')

        # Merge with existing data (custom translations take precedence)
        current_df = self._translation_df if self._translation_df is not None else pd.DataFrame()

        if len(current_df) > 0:
            # Update existing entries and add new ones
            self._translation_df = pd.concat([current_df, custom_df]).groupby(level=0).last()
        else:
            self._translation_df = custom_df

        logger.info(f"Added {len(custom_translations)} custom translations")

    def validate_data(self) -> bool:
        """Validate that all required data files are available"""
        try:
            # Trigger loading of all properties
            # TODO
            '''
            _ = self.domains
            '''
            _ = self.subtypes
            _ = self.sde_schema
            _ = self.translation_df
            return True
        except FileNotFoundError as e:
            logger.error(f"Data validation failed: {e}")
            return False


def get_default_config() -> GeoDataConfig:
    """Get default configuration instance"""
    return GeoDataConfig()