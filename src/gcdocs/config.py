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
from rich.console import Console

console = Console()


AVAILABLE_LANGUAGES = ["de", "fr", "it", "en"]


def parse_langs(ctx, param, value):
    if not value:
        raise click.BadParameter("You must provide at least one language.")
    langs = [v.strip().lower() for v in value.split(",")]

    invalid = [lang for lang in langs if lang not in AVAILABLE_LANGUAGES]
    if invalid:
        raise click.BadParameter(f"Invalid language(s): {', '.join(invalid)}")
    return langs


abreviations = [
    "Aarc",
    "Aart",
    "Abor",
    "Aexp",
    "Gall",
    "Gero",
    "Ggla",
    "Gins",
    "Gkar",
    "Hcon",
    "Hpal",
    "Hsub",
    "Hsur",
    "Lano",
    "Lfos",
    "Lgeo",
    "Lmin",
    "Lmis",
    "Lpro",
    "LresLsed",
    "Ltyp",
    "Mfol",
    "Mlin",
    "Mpla",
    "Pcon",
    "Pmod",
    "Pslo",
    "Rbed",
    "Runc",
    "Tdef",
    "Ttec",
]

tables = [
    "Admixtures.csv",
    "Charcat.csv",
    "Chrono.csv",
    "Composit.csv",
    "Litho.csv",
    "Litstrat.csv",
]

IGNORE_FIELDS = [
    "OPERATOR",
    "DATEOFCREATION",
    "DATEOFCHANGE",
    "CREATION_YEAR",
    "CREATION_MONTH",
    "REVISION_YEAR",
    "REVISION_MONTH",
    "REASONFORCHANGE",
    "OBJECTORIGIN",
    "OBJECTORIGIN_YEAR",
    "OBJECTORIGIN_MONTH",
    "KIND",
    "RC_ID",
    "WU_ID",
    "RC_ID_CREATION",
    "WU_ID_CREATION",
    "REVISION_QUALITY",
    "ORIGINAL_ORIGIN",
    "INTEGRATION_OBJECT_UUID",
    "SHAPE.AREA",
    "SHAPE.LEN",
    "MORE_INFO",
]

ATTRIBUTES_TO_IGNORE = [
    "CREATION_MONTH",
    "CREATION_YEAR",
    "DATEOFCHANGE",
    "DATEOFCREATION",
    "OBJECTORIGIN_MONTH",
    "OBJECTORIGIN_YEAR",
    "OPERATOR",
    "ORIGINAL_ORIGIN",
    "PRINTEDOBJECTORIGIN",
    "RC_ID",
    "RC_ID_CREATION",
    "REASONFORCHANGE",
    "REVISION_MONTH",
    "REVISION_QUALITY",
    "REVISION_YEAR",
    "SHAPE",
    "SHAPE.AREA",
    "SHAPE.LEN",
    "UUID",
    "WU_ID",
    "WU_ID_CREATION",
]


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

        def extract_coded_values(data):
            """
            Extracts and flattens all codedValues from coded_domain entries
            whose keys start with 'GC_'.

            Returns:
                dict: A flat dictionary of code-value pairs.
            """
            coded = data.get("coded_domain", {})

            flat = {
                code: label
                for domain_key, domain_data in coded.items()
                if domain_key.startswith("GC_")
                for code, label in domain_data.get("codedValues", {}).items()
            }

            return dict(sorted(flat.items(), key=lambda item: int(item[0])))

        if self._domains is None:
            self._domains = extract_coded_values(self.sde_schema)
            domains_file = self.input_dir / "coded_domains.json"
            if not domains_file.exists():
                with open(domains_file, "w", encoding="utf-8") as f:
                    json.dump(self._domains, f, indent=4)
                    logger.info(f"Saved domains to {domains_file}")
        return self._domains

    '''@property
    def domains(self) -> Dict[str, Any]:
        """Load coded domains (replaces global 'domains')"""
        if self._domains is None:
            domains_file = self.input_dir / "coded_domains.json"
            if not domains_file.exists():
                raise FileNotFoundError(f"Domains file not found: {domains_file}")

            with open(domains_file, "r") as f:
                self._domains = json.load(f)
            logger.info(f"Loaded domains from {domains_file}")
        return self._domains'''

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
        logger.debug("=== Loading translations ===")
        try:
            dataframes = []

            # 1. Load JSON coded domains (fallback German -> French)
            code_dict = self.domains
            if code_dict:
                df_json = pd.DataFrame(
                    {
                        "GeolCodeInt": list(code_dict.keys()),
                        "DE": list(code_dict.values()),
                        "FR": list(
                            code_dict.values()
                        ),  # Use German as fallback for French
                    }
                )
                df_json["IT"] = None
                df_json["EN"] = None
                df_json["GeolCodeInt"] = df_json["GeolCodeInt"].astype("string")
                df_json["source"] = "coded_domains"
                dataframes.append(df_json)
                logger.debug(f"Loaded JSON translations: {len(df_json)} entries")

            """# 2. Load CSV translation file (legacy/main source)
            csv_file = self._find_file("GeolCodeText_Trad_230317.csv")
            if csv_file:
                df_csv = pd.read_csv(csv_file, sep=";")
                df_csv["GeolCodeInt"] = df_csv["GeolCodeInt"].astype("string")
                dataframes.append(df_csv)
                logger.debug(f"Loaded CSV translations: {len(df_csv)} entries")"""

            # 3. Load new Excel translations (if available)
            trad_fname = "_GeolCodeText_Trad.xlsx"
            excel_file = self._find_file(trad_fname)
            if excel_file:
                df_excel = pd.read_excel(excel_file, sheet_name="Tabelle1")
                df_excel["GeolCodeInt"] = df_excel["GeolCodeInt"].astype("string")
                df_excel["source"] = trad_fname
                dataframes.append(df_excel)
                logger.debug(df_excel.head(5))
                logger.info(
                    f"Loaded Excel translations from {excel_file.resolve()}: {len(df_excel)} entries"
                )

            # 4. Load custom chronology translations (if available)
            chrono_file = self._find_file("geolcode_chrono.csv")
            if chrono_file:
                df_chrono = pd.read_csv(chrono_file)
                df_chrono["GeolCodeInt"] = df_chrono["GeolCodeInt"].astype("string")
                df_chrono["source"] = "geolcode_chrono"
                dataframes.append(df_chrono)
                logger.debug(df_chrono.head(5))
                logger.info(
                    f"Loaded chrono translations from {chrono_file.resolve()}: {len(df_chrono)} entries"
                )
            else:
                logger.warning(f"No file `geolcode_chrono.csv` found" )

            # 5. Load application UI translations (if available)
            app_translations = self._find_file("translations.xlsx")
            if app_translations:
                df_app = pd.read_excel(
                    app_translations, usecols=["msg_id", "de", "fr", "it", "en"]
                )
                df_app.columns = df_app.columns.str.upper()
                df_app.rename(columns={"MSG_ID": "GeolCodeInt"}, inplace=True)
                df_app["GeolCodeInt"] = df_app["GeolCodeInt"].astype("string")

                df_app = pd.concat(
                    [
                        df_app,
                        pd.DataFrame(
                            [
                                {
                                    "GeolCodeInt": "current_lang",
                                    "DE": "Deutsch",
                                    "FR": "Français",
                                    "IT": "Italiano",
                                    "EN": "English",
                                }
                            ]
                        ),
                    ],
                    ignore_index=True,
                )

                df_app["source"] = "translations"
                dataframes.append(df_app)
                logger.debug(df_app.head(5))

                logger.info(
                    f"Loaded app translations from {app_translations.resolve()}: {len(df_app)} entries"
                )

            # 6. Add special hardcoded values
            special_codes = pd.DataFrame(
                [
                    {
                        "GeolCodeInt": "999997",
                        "DE": "unbekannt",
                        "FR": "inconnu",
                        "IT": "sconosciuto",
                        "EN": "unknown",
                    },
                    {
                        "GeolCodeInt": "999998",
                        "DE": "nicht anwendbar",
                        "FR": "pas applicable",
                        "IT": "non applicabile",
                        "EN": "not applicable",
                    },
                    {
                        "GeolCodeInt": "11401005",
                        "DE": "Kame",
                        "FR": "kame",
                        "IT": "kame",
                        "EN": "kame",
                    },
                ]
            )
            special_codes["GeolCodeInt"] = special_codes["GeolCodeInt"].astype("string")
            special_codes["source"] = "special"
            dataframes.append(special_codes)

            if not dataframes:
                logger.warning("No translation files found, creating empty DataFrame")
                return pd.DataFrame(columns=AVAILABLE_LANGUAGES).astype("string")

            # Merge all dataframes
            merged_df = pd.concat(dataframes, ignore_index=True)

            # Clean and process
            translation_df = self._clean_translation_data(merged_df, debug_export=True)

            logger.info(
                f"Loaded merged translations: {len(translation_df)} total entries"
            )
            return translation_df

        except Exception as e:
            import traceback
            logger.error(f"Failed to load translation data: {e}")
            logger.error(traceback.format_exc())

            # Return minimal DataFrame with special codes
            return pd.DataFrame(
                [
                    {"GeolCodeInt": "999997", "DE": "unbekannt", "FR": "inconnu"},
                    {
                        "GeolCodeInt": "999998",
                        "DE": "nicht anwendbar",
                        "FR": "pas applicable",
                        "IT": "non applicabile",
                        "EN": "not applicable",
                    },
                ]
            ).set_index("GeolCodeInt")

    def _find_file(self, filename: str) -> Optional[Path]:
        """Find a file in the input directory or package data"""
        # Try input directory first
        current_path = None

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

        logger.error(f"Translation file not found: {filename}")
        return None

    def _clean_translation_data(
        self, merged_df: pd.DataFrame, debug_export: bool = False
    ) -> pd.DataFrame:
        """Clean and process the merged translation DataFrame

        Args:
            merged_df: DataFrame to clean
            debug_export: If True, export discarded data to Excel files
        """
        from datetime import datetime

        required_cols = ["GeolCodeInt", "DE", "FR", "IT", "EN", "source"]
        for col in required_cols:
            if col not in merged_df.columns:
                merged_df[col] = ""

        initial_count = len(merged_df)
        df_work = merged_df[required_cols].copy()

        # === DEBUG: Export duplicates ===
        if debug_export:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            debug_file = self.input_dir / f"debug_discarded_{timestamp}.xlsx"

            # Find duplicates (those that will be removed)
            duplicates = df_work[
                df_work.duplicated(subset=["GeolCodeInt"], keep="last")
            ]

            # Apply deduplication to continue
            df_deduped = df_work.drop_duplicates(subset=["GeolCodeInt"], keep="last")

            # Apply cleaning transformations
            df_cleaned = df_deduped.assign(
                GeolCodeInt=lambda x: x["GeolCodeInt"].astype("string"),
                source=lambda x: x["source"].astype("string"),
                DE=lambda x: x["DE"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
                FR=lambda x: x["FR"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
                IT=lambda x: x["IT"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
                EN=lambda x: x["EN"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
            )

            # Find empty codes (those that will be removed)
            empty_codes = df_cleaned[
                (df_cleaned["GeolCodeInt"] == "") | (df_cleaned["GeolCodeInt"] == "nan")
            ]

            # Create summary
            summary_data = {
                "Category": [
                    "Initial rows",
                    "Duplicates removed",
                    "Empty codes removed",
                    "Final rows",
                ],
                "Count": [
                    initial_count,
                    len(duplicates),
                    len(empty_codes),
                    len(df_cleaned) - len(empty_codes),
                ],
            }
            summary_df = pd.DataFrame(summary_data)

            # Write to Excel with multiple sheets
            with pd.ExcelWriter(debug_file, engine="openpyxl") as writer:
                summary_df.to_excel(writer, sheet_name="Summary", index=False)

                if len(duplicates) > 0:
                    duplicates.to_excel(writer, sheet_name="Duplicates", index=False)

                if len(empty_codes) > 0:
                    empty_codes.to_excel(writer, sheet_name="Empty_Codes", index=False)

            logger.info(f"Debug data exported to: {debug_file}")
            logger.info(f"  - Duplicates: {len(duplicates)}")
            logger.info(f"  - Empty codes: {len(empty_codes)}")
            logger.info(f"  - Total discarded: {len(duplicates) + len(empty_codes)}")

        # === Normal cleaning process ===
        cleaned_df = (
            df_work.drop_duplicates(subset=["GeolCodeInt"], keep="last")
            .assign(
                GeolCodeInt=lambda x: x["GeolCodeInt"].astype("string"),
                source=lambda x: x["source"].astype("string"),
                DE=lambda x: x["DE"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
                FR=lambda x: x["FR"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
                IT=lambda x: x["IT"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
                EN=lambda x: x["EN"]
                .astype("string")
                .replace(["0", "nan", "None"], "-"),
            )
            .query("GeolCodeInt != '' and GeolCodeInt != 'nan'")
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

        if df is None or df.empty:
            return self._get_empty_stats()

        languages = ["DE", "FR", "IT", "EN"]

        # Validate columns
        for lang in languages:
            if lang not in df.columns:
                raise ValueError(f"Missing required column: {lang}")

        # Create boolean masks for missing values
        missing_masks = {}
        present_masks = {}

        for lang in languages:
            # Combine multiple missing conditions
            missing_mask = (
                (df[lang] == "-")
                | (df[lang] == "")
                | df[lang].isna()
                | (
                    df[lang].isnull()
                    if hasattr(df[lang], "isnull")
                    else pd.isnull(df[lang])
                )
            )
            missing_masks[lang] = missing_mask
            present_masks[lang] = ~missing_mask

        # Calculate complete entries (all languages present)
        complete_mask = (
            present_masks["DE"]
            & present_masks["FR"]
            & present_masks["IT"]
            & present_masks["EN"]
        )
        complete_entries = complete_mask.sum()
        total_entries = len(df)

        stats = {"total_entries": total_entries}

        # Add translations and missing counts for each language
        for lang in languages:
            stats[f"{lang.lower()}_translations"] = present_masks[lang].sum()
            stats[f"missing_{lang.lower()}"] = missing_masks[lang].sum()

        # Add complete and missing translation counts
        stats["complete_entries"] = complete_entries
        stats["missing_translation"] = total_entries - complete_entries

        return stats

    def add_custom_translations(self, custom_translations: Dict[str, Dict[str, str]]):
        """Add custom translations to the existing DataFrame

        Args:
            custom_translations: Dict like {"123": {"DE": "German text", "FR": "French text"}}
        """
        if not custom_translations:
            return

        custom_df = pd.DataFrame.from_dict(custom_translations, orient="index")
        custom_df.index.name = "GeolCodeInt"
        custom_df.index = custom_df.index.astype("string")

        # Merge with existing data (custom translations take precedence)
        current_df = (
            self._translation_df if self._translation_df is not None else pd.DataFrame()
        )

        if len(current_df) > 0:
            # Update existing entries and add new ones
            self._translation_df = (
                pd.concat([current_df, custom_df]).groupby(level=0).last()
            )
        else:
            self._translation_df = custom_df

        logger.info(f"Added {len(custom_translations)} custom translations")

    def validate_data(self) -> bool:
        """Validate that all required data files are available"""
        try:
            # Trigger loading of all properties
            # TODO
            """
            _ = self.domains
            """
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
