import unittest
from unittest.mock import patch, MagicMock


import sys

# Mock 'arcpy' before importing your module
import sys

sys.modules["arcpy"] = MagicMock()
arcpy = sys.modules["arcpy"]
arcpy.env = MagicMock()  # Explicitly mock 'arcpy.env'
arcpy.da = MagicMock()  # Explicitement moquer 'arcpy.da'

from schema import GeocoverSchema, gc_filter  # Import the class you want to test


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


class TestGeocoverSchema(unittest.TestCase):
    def setUp(self):
        # Reset the singleton instance before each test
        GeocoverSchema._GeocoverSchema__instance = None

    @patch("arcpy.env", new_callable=MagicMock)
    @patch("arcpy.ListTables")
    def test_init(self, mock_list_tables, mock_env):
        # Define mock behavior
        mock_list_tables.return_value = ["table1", "table2"]

        # Test instance creation
        instance = GeocoverSchema("fake_workspace")

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
        with patch("schema.gc_filter", mock_gc_filter):
            # Create an instance of GeocoverSchema
            instance = GeocoverSchema("fake_workspace")

            # Call the tables_list property
            result = instance.tables_list

            # Check if the result matches the filtered list
            self.assertEqual(result, ["table1", "table2"])

    @patch("arcpy.env", new_callable=MagicMock)
    @patch("arcpy.da.ListDomains")
    def test_list_coded_domains(self, mock_list_domains, mock_env):
        # Définir un comportement simulé pour ListDomains
        mock_domain1 = MagicMock(name="Domain1")
        mock_domain1.name = "GC_Domain1"
        mock_domain2 = MagicMock(name="Domain2")
        mock_domain2.name = "Non_Valid_Domain"
        mock_domain3 = MagicMock(name="Domain3")
        mock_domain3.name = "GC_Domain3"

        # Liste simulée de domaines
        mock_list_domains.return_value = [mock_domain1, mock_domain2, mock_domain3]

        # Assuming gc_prefix_filter only allows name starting with 'GC_'
        def mock_gc_prefix_filter(domain_name):
            return domain_name.name.startswith("GC_")

        # Replace the actual gc_prefix_filter with the mock version
        with patch("schema.gc_prefix_filter", mock_gc_prefix_filter):
            # Create an instance of GeocoverSchema
            instance = GeocoverSchema("fake_workspace")

            # Call the list_coded_domains property
            result = instance.list_coded_domains()

            # Check if the result matches the filtered list
            self.assertEqual(
                result, [mock_domain1, mock_domain3]
            )  # Devrait contenir uniquement les domaines commençant par "GC_"

            # Vérifier que ListDomains a été appelé avec le bon espace de travail
            arcpy.da.ListDomains.assert_called_with(instance._GeocoverSchema__workspace)

    @patch.object(GeocoverSchema, "list_coded_domains")
    def test_coded_domains_esri_style_dump_false(self, mock_list_coded_domains):
        # Use the helper function to create mock domains
        mock_list_coded_domains.return_value = create_mock_domains()

        # Create instance
        instance = GeocoverSchema("fake_workspace")
        instance.esri_style_dump = False  # Set the property to False

        # Call the property
        result = instance.coded_domains

        # Verify expected results
        expected_result = {
            "GC_Domain1": {"1": "Value1", "2": "Value2"},
            "GC_Domain2": {
                "type": "Range",
                "codedValues": {"RangeStart": 10, "RangeEnd": 20},
            },
        }

        self.assertEqual(result, expected_result)

    @patch.object(GeocoverSchema, "list_coded_domains")
    def test_coded_domains_esri_style_dump_true(self, mock_list_coded_domains):
        # Use the helper function to create mock domains
        mock_list_coded_domains.return_value = create_mock_domains()

        # Create instance
        instance = GeocoverSchema("fake_workspace")
        instance.esri_style_dump = True  # Set the property to True

        # Call the property
        result = instance.coded_domains

        # Verify expected results
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


if __name__ == "__main__":
    unittest.main()
