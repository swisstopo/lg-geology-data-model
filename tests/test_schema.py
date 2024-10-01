import unittest
from unittest.mock import patch, MagicMock


import sys
import sys

# Mock 'arcpy' before importing geocover
sys.modules["arcpy"] = MagicMock()
arcpy = sys.modules["arcpy"]
arcpy.env = MagicMock()
arcpy.da = MagicMock()

from geocover import schema


def create_mock_domains():
    """Helper function to create mock domain objects."""
    mock_domain1 = MagicMock(name="Domain1")
    mock_domain1.name = "GC_Domain1"
    mock_domain1.domainType = "CodedValue"
    mock_domain1.codedValues = {"1": "Value1", "2": "Value2"}

    mock_domain2 = MagicMock(name="Domain2")
    mock_domain2.name = "GC_Domain2"
    mock_domain2.domainType = "Range"
    mock_domain2.codedValues = {"RangeStart": 10, "RangeEnd": 20}

    return [mock_domain1, mock_domain2]


def create_mock_fields():
    """Helper function to create mock field objects."""
    mock_field1 = MagicMock(name="Field1")
    mock_field1.name = "Field1"
    mock_field1.type = "String"
    mock_field1.length = 50
    mock_field1.domain = "GC_Domain1"  # This matches one of our coded domain values

    mock_field2 = MagicMock(name="Field2")
    mock_field2.name = "Field2"
    mock_field2.type = "Integer"
    mock_field2.length = 10
    mock_field2.domain = ""  # No domain associated

    return [mock_field1, mock_field2]


class TestGeocoverSchema(unittest.TestCase):
    def setUp(self):
        # Reset the singleton instance before each test
        schema.GeocoverSchema._GeocoverSchema__instance = None

    @patch("arcpy.env", new_callable=MagicMock)
    @patch("arcpy.ListTables")
    def test_init(self, mock_list_tables, mock_env):
        # Define mock behavior
        mock_list_tables.return_value = ["table1", "table2"]

        # Test instance creation
        instance = schema.GeocoverSchema("fake_workspace")

        # Check if the workspace was set correctly
        self.assertEqual(instance._GeocoverSchema__workspace, "fake_workspace")
        mock_env.workspace = "fake_workspace"

    @patch("arcpy.env", new_callable=MagicMock)
    @patch("arcpy.ListTables")
    def test_tables_list(self, mock_list_tables, mock_env):
        # Define mock behavior with tables that match the gc_filter criteria
        mock_list_tables.return_value = ["table1", "table2", "invalid_table"]

        # Assuming gc_filter only allows tables starting with 'table'
        def mock_gc_filter(table_name):
            return table_name.startswith("table")

        # Replace the actual gc_filter with the mock version
        with patch("geocover.schema.gc_filter", mock_gc_filter):
            instance = schema.GeocoverSchema("fake_workspace")

            result = instance.tables_list

            self.assertEqual(result, ["table1", "table2"])

    @patch("arcpy.env", new_callable=MagicMock)
    @patch("arcpy.da.ListDomains")
    def test_list_coded_domains(self, mock_list_domains, mock_env):
        # mock for ListDomains
        mock_domain1 = MagicMock(name="Domain1")
        mock_domain1.name = "GC_Domain1"
        mock_domain2 = MagicMock(name="Domain2")
        mock_domain2.name = "Non_Valid_Domain"
        mock_domain3 = MagicMock(name="Domain3")
        mock_domain3.name = "GC_Domain3"

        mock_list_domains.return_value = [mock_domain1, mock_domain2, mock_domain3]

        # Assuming gc_prefix_filter only allows name starting with 'GC_'
        def mock_gc_prefix_filter(domain_name):
            return domain_name.name.startswith("GC_")

        with patch("geocover.schema.gc_prefix_filter", mock_gc_prefix_filter):
            instance = schema.GeocoverSchema("fake_workspace")

            result = instance.list_coded_domains()

            self.assertEqual(
                result, [mock_domain1, mock_domain3]
            )  # Only domains beginning with "GC_"

            arcpy.da.ListDomains.assert_called_with(instance._GeocoverSchema__workspace)

    @patch.object(schema.GeocoverSchema, "list_coded_domains")
    def test_coded_domains_esri_style_dump_false(self, mock_list_coded_domains):
        mock_list_coded_domains.return_value = create_mock_domains()

        instance = schema.GeocoverSchema("fake_workspace")
        instance.esri_style_dump = False  # Set the property to False

        result = instance.coded_domains

        expected_result = {
            "GC_Domain1": {"1": "Value1", "2": "Value2"},
            "GC_Domain2": {
                "type": "Range",
                "codedValues": {"RangeStart": 10, "RangeEnd": 20},
            },
        }

        self.assertEqual(result, expected_result)

    @patch.object(schema.GeocoverSchema, "list_coded_domains")
    def test_coded_domains_esri_style_dump_true(self, mock_list_coded_domains):
        mock_list_coded_domains.return_value = create_mock_domains()

        instance = schema.GeocoverSchema("fake_workspace")
        instance.esri_style_dump = True  # Set the property to True

        result = instance.coded_domains

        expected_result = {
            "GC_Domain1": {
                "type": "CodedValue",
                "codedValues": {"1": "Value1", "2": "Value2"},
            },
            "GC_Domain2": {
                "type": "Range",
                "codedValues": {"RangeStart": 10, "RangeEnd": 20},
            },
        }

        self.assertEqual(result, expected_result)

    @patch("arcpy.ListFields")
    @patch.object(schema.GeocoverSchema, "list_coded_domains")
    def test_fields(self, mock_list_coded_domains, mock_list_fields):
        mock_list_fields.return_value = create_mock_fields()

        mock_list_coded_domains.return_value = [
            MagicMock(
                name="GC_Domain1",
                domainType="CodedValue",
                codedValues={1: "Value1", 2: "Value2"},
            ),
            MagicMock(
                name="GC_Domain2",
                domainType="CodedValue",
                codedValues={3: "Value3", 4: "Value4"},
            ),
        ]

        instance = schema.GeocoverSchema("fake_workspace")

        instance._GeocoverSchema__coded_domains_values = {
            "GC_Domain1": {
                "type": "CodedValue",
                "codedValues": {1: "Value1", 2: "Value2"},
            },
            "GC_Domain2": {
                "type": "CodedValue",
                "codedValues": {3: "Value3", 4: "Value4"},
            },
        }

        result = instance.fields("fake_feature_class")

        expected_result = [
            {"name": "Field1", "type": "String", "length": 50, "domain": "GC_Domain1"},
            {
                "name": "Field2",
                "type": "Integer",
                "length": 10,
                "domain": None,  # No domain for this field
            },
        ]

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
