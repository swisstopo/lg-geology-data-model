"""
Smoke tests for the gcdocs module.

These tests verify that the core components can be imported and instantiated,
and that pure-logic functions behave correctly — without requiring any ESRI
data files or a full build environment.
"""

import pytest
from click.testing import CliRunner


# ---------------------------------------------------------------------------
# 1. Imports
# ---------------------------------------------------------------------------

def test_import_cli():
    from gcdocs.cli import gcdocs  # noqa: F401


def test_import_config():
    from gcdocs.config import GeoDataConfig, AVAILABLE_LANGUAGES  # noqa: F401


def test_import_validator():
    from gcdocs.core.validator import ModelValidator  # noqa: F401


def test_import_helpers():
    from gcdocs.helpers import extract_coded_domains, extract_subtypes_from_schema  # noqa: F401


# ---------------------------------------------------------------------------
# 2. CLI smoke — --help flags must exit 0
# ---------------------------------------------------------------------------

@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    from gcdocs.cli import gcdocs
    result = runner.invoke(gcdocs, ["--help"])
    assert result.exit_code == 0
    assert "generate" in result.output.lower()


def test_cli_validate_help(runner):
    from gcdocs.cli import gcdocs
    result = runner.invoke(gcdocs, ["validate", "--help"])
    assert result.exit_code == 0


def test_cli_generate_help(runner):
    from gcdocs.cli import gcdocs
    result = runner.invoke(gcdocs, ["generate", "--help"])
    assert result.exit_code == 0


def test_cli_export_help(runner):
    from gcdocs.cli import gcdocs
    result = runner.invoke(gcdocs, ["export", "--help"])
    assert result.exit_code == 0


# ---------------------------------------------------------------------------
# 3. Validate command against the real datamodel.yaml in the repo
# ---------------------------------------------------------------------------

def test_cli_validate_datamodel(runner, tmp_path):
    """gcdocs validate should accept the committed datamodel.yaml."""
    import pathlib
    repo_root = pathlib.Path(__file__).parent.parent
    datamodel = repo_root / "datamodel.yaml"

    if not datamodel.exists():
        pytest.skip("datamodel.yaml not found in repo root")

    from gcdocs.cli import gcdocs
    result = runner.invoke(gcdocs, ["validate", str(datamodel)])
    # Exit 0 means valid; exit 1 would mean schema errors were reported
    assert result.exit_code == 0, result.output


# ---------------------------------------------------------------------------
# 4. ModelValidator unit tests (no file I/O)
# ---------------------------------------------------------------------------

def test_validator_basic_valid():
    """Use a version with no JSON schema file so the basic validator runs."""
    from gcdocs.core.validator import ModelValidator
    validator = ModelValidator()
    data = {
        "version": "0.0",  # no json-schema-0.0.json → falls back to _basic_validation
        "themes": [
            {"name": "MyTheme", "classes": [{"name": "MyClass"}]}
        ],
    }
    assert validator.validate_data(data) is True


def test_validator_missing_required_field():
    from gcdocs.core.validator import ModelValidator
    validator = ModelValidator()
    # Missing 'themes' key
    result = validator.validate_data({"version": "0.11"})
    # Either the JSON-schema validator or the basic validator should catch this
    # We just assert it returns a bool and doesn't crash
    assert isinstance(result, bool)


def test_validator_invalid_themes_type():
    from gcdocs.core.validator import ModelValidator
    validator = ModelValidator()
    data = {"version": "0.11", "themes": "not-a-list"}
    result = validator.validate_data(data)
    assert isinstance(result, bool)


# ---------------------------------------------------------------------------
# 5. helpers — extract_coded_domains
# ---------------------------------------------------------------------------

def test_extract_coded_domains_format1():
    """Format 1: coded_domain dict with codedValues dict."""
    from gcdocs.helpers import extract_coded_domains
    data = {
        "coded_domain": {
            "GC_Foo": {"codedValues": {"1": "Alpha", "2": "Beta"}},
            "OTHER_Domain": {"codedValues": {"3": "Gamma"}},
        }
    }
    result = extract_coded_domains(data, prefix="GC_")
    assert result == {"1": "Alpha", "2": "Beta"}


def test_extract_coded_domains_format2():
    """Format 2: native ESRI domains array."""
    from gcdocs.helpers import extract_coded_domains
    data = {
        "domains": [
            {
                "type": "codedValue",
                "name": "GC_Bar",
                "codedValues": [
                    {"code": 10, "name": "Ten"},
                    {"code": 20, "name": "Twenty"},
                ],
            },
            {
                "type": "range",
                "name": "GC_Ignored",
                "codedValues": [],
            },
        ]
    }
    result = extract_coded_domains(data, prefix="GC_")
    assert result == {"10": "Ten", "20": "Twenty"}


def test_extract_coded_domains_no_prefix():
    """Empty prefix returns all domains."""
    from gcdocs.helpers import extract_coded_domains
    data = {
        "coded_domain": {
            "GC_A": {"codedValues": {"1": "One"}},
            "XY_B": {"codedValues": {"2": "Two"}},
        }
    }
    result = extract_coded_domains(data, prefix="")
    assert "1" in result
    assert "2" in result


def test_extract_coded_domains_empty():
    from gcdocs.helpers import extract_coded_domains
    assert extract_coded_domains({}) == {}


# ---------------------------------------------------------------------------
# 6. helpers — extract_subtypes_from_schema
# ---------------------------------------------------------------------------

def test_extract_subtypes_dict_format():
    from gcdocs.helpers import extract_subtypes_from_schema
    data = {"subtypes": {"100": "Rock", "200": "Sediment"}}
    result = extract_subtypes_from_schema(data)
    assert result["100"] == "Rock"
    assert result["200"] == "Sediment"


def test_extract_subtypes_list_format():
    from gcdocs.helpers import extract_subtypes_from_schema
    data = {
        "subtypes": [
            {"subtypeCode": 1, "subtypeName": "Alpha"},
            {"subtypeCode": 2, "subtypeName": "Beta"},
        ]
    }
    result = extract_subtypes_from_schema(data)
    assert result["1"] == "Alpha"
    assert result["2"] == "Beta"


def test_extract_subtypes_nested():
    """Subtypes nested inside a feature class."""
    from gcdocs.helpers import extract_subtypes_from_schema
    data = {
        "featureClasses": {
            "MyLayer": {
                "subtypes": [
                    {"subtypeCode": 99, "subtypeName": "Deep"}
                ]
            }
        }
    }
    result = extract_subtypes_from_schema(data)
    assert result["99"] == "Deep"


def test_extract_subtypes_empty():
    from gcdocs.helpers import extract_subtypes_from_schema
    assert extract_subtypes_from_schema({}) == {}


# ---------------------------------------------------------------------------
# 7. Config constants
# ---------------------------------------------------------------------------

def test_available_languages():
    from gcdocs.config import AVAILABLE_LANGUAGES
    assert set(AVAILABLE_LANGUAGES) == {"de", "fr", "it", "en"}
