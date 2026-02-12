"""
Model validation for gcdocs
Extracted from original datamodel.py validation logic
"""

import json
import yaml
from pathlib import Path
from typing import List, Optional
from loguru import logger


class ModelValidator:
    """Validates YAML datamodels against JSON schema"""

    def __init__(self, schema_dir: Optional[str] = None):
        self.schema_dir = Path(schema_dir) if schema_dir else self._find_schema_dir()
        self.errors: List[str] = []

    def _find_schema_dir(self) -> Path:
        """Find the schema directory"""
        # Try package schema directory first
        try:
            from importlib import resources
            with resources.path("gcdocs.schemas", "") as schema_path:
                if schema_path.exists():
                    return schema_path
        except (ImportError, FileNotFoundError):
            pass

        # Try relative to current file
        schema_dir = Path(__file__).parent.parent / "schemas"
        if schema_dir.exists():
            return schema_dir

        # Try current directory
        schema_dir = Path("schema")
        if schema_dir.exists():
            return schema_dir

        raise FileNotFoundError("Schema directory not found")

    def validate_file(self, yaml_file: str) -> bool:
        """Validate a YAML file against its schema"""
        self.errors.clear()

        try:
            # Load YAML data
            with open(yaml_file, 'r', encoding='utf-8') as f:
                yaml_data = yaml.safe_load(f)

            return self.validate_data(yaml_data)

        except yaml.YAMLError as e:
            self.errors.append(f"YAML parsing error: {e}")
            return False
        except FileNotFoundError as e:
            self.errors.append(f"File not found: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Validation error: {e}")
            return False

    def validate_data(self, yaml_data: dict) -> bool:
        """Validate YAML data against schema"""
        try:
            from jsonschema import Draft7Validator, ValidationError

            # Get schema version from data
            version = yaml_data.get("version", "0.9")  # Default version
            schema_file = self.schema_dir / f"json-schema-{version}.json"

            if not schema_file.exists():
                self.errors.append(f"Schema file not found: {schema_file}")
                logger.warning(f"Schema file not found: {schema_file}")
                # Try to continue without strict validation
                return self._basic_validation(yaml_data)

            # Load schema
            with open(schema_file, 'r', encoding='utf-8') as f:
                schema_data = json.load(f)

            # Validate
            validator = Draft7Validator(schema_data)
            errors = sorted(validator.iter_errors(yaml_data), key=lambda e: e.path)

            if errors:
                for error in errors:
                    error_path = " -> ".join(str(p) for p in error.path)
                    self.errors.append(f"At {error_path}: {error.message}")
                    logger.error(f"Validation error at {error_path}: {error.message}")
                return False

            logger.info("YAML data is valid according to schema")
            return True

        except ImportError:
            logger.warning("jsonschema not available, using basic validation")
            return self._basic_validation(yaml_data)
        except Exception as e:
            self.errors.append(f"Schema validation failed: {e}")
            logger.error(f"Schema validation failed: {e}")
            return False

    def _basic_validation(self, yaml_data: dict) -> bool:
        """Basic validation when jsonschema is not available"""
        required_fields = ["version", "themes"]

        for field in required_fields:
            if field not in yaml_data:
                self.errors.append(f"Missing required field: {field}")
                return False

        # Check themes structure
        themes = yaml_data.get("themes", [])
        if not isinstance(themes, list):
            self.errors.append("'themes' must be a list")
            return False

        for i, theme in enumerate(themes):
            if not isinstance(theme, dict):
                self.errors.append(f"Theme {i} must be a dictionary")
                return False

            if "name" not in theme:
                self.errors.append(f"Theme {i} missing 'name' field")
                return False

            classes = theme.get("classes", [])
            if not isinstance(classes, list):
                self.errors.append(f"Theme {i} 'classes' must be a list")
                return False

            for j, cls in enumerate(classes):
                if not isinstance(cls, dict):
                    self.errors.append(f"Theme {i}, class {j} must be a dictionary")
                    return False

                if "name" not in cls:
                    self.errors.append(f"Theme {i}, class {j} missing 'name' field")
                    return False

        logger.info("Basic validation passed")
        return True

    def get_errors(self) -> List[str]:
        """Get list of validation errors"""
        return self.errors.copy()

    def clear_errors(self):
        """Clear validation errors"""
        self.errors.clear()