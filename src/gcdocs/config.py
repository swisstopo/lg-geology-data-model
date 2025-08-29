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
        """Load translation DataFrame (replaces global 'df')"""
        if self._translation_df is None:
            # Try package data first, then input_dir
            translation_file = self._find_translation_file()

            self._translation_df = pd.read_csv(translation_file, sep=";")
            self._translation_df = self._translation_df.set_index(["GeolCodeInt"])
            logger.info(f"Loaded translations from {translation_file}")
        return self._translation_df

    def _find_translation_file(self) -> Path:
        """Find the translation CSV file"""
        filename = "GeolCodeText_Trad_230317.csv"

        # Try input_dir first
        input_path = self.input_dir / filename
        if input_path.exists():
            return input_path

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

        raise FileNotFoundError(f"Translation file not found: {filename}")

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