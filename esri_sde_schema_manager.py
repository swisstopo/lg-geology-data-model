import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

from loguru import logger


@dataclass
class CodedValue:
    """Represents a single coded value in a domain."""

    name: str
    code: int


@dataclass
class Domain:
    """Represents a domain in the ESRI SDE schema."""

    type: str
    name: str
    description: str
    coded_values: List[CodedValue] = field(default_factory=list)


@dataclass
class Dataset:
    """Represents a dataset in the ESRI SDE schema."""

    name: str
    type: str
    additional_info: Dict[str, Any] = field(default_factory=dict)
    nested_datasets: List["Dataset"] = field(default_factory=list)


class ESRISchemaManager:
    def __init__(self, schema_file_path: str):
        with open(schema_file_path, "r", encoding="utf-8") as file:
            self.schema = json.load(file)

        self.domains = self._parse_domains()
        self.datasets = self._parse_datasets(self.schema.get("datasets", []))

    def _parse_domains(self) -> List[Domain]:
        """
        Parse domains from the schema.

        :return: List of Domain objects
        """
        domains = []
        for domain_data in self.schema.get("domains", []):
            coded_values = [
                CodedValue(name=cv["name"], code=cv["code"])
                for cv in domain_data.get("codedValues", [])
            ]

            domains.append(
                Domain(
                    type=domain_data.get("type", ""),
                    name=domain_data.get("name", ""),
                    description=domain_data.get("description", ""),
                    coded_values=coded_values,
                )
            )

        return domains

    def _parse_datasets(self, dataset_list: List[Dict[str, Any]]) -> List[Dataset]:
        datasets = []
        for dataset_data in dataset_list:
            # Create current dataset
            dataset_name = dataset_data.get("name", "")
            if dataset_name.startswith(('TOPGIS_GC', 'GC_',)):
              if not dataset_name.endswith("_I"):
                dataset = Dataset(
                    name=dataset_name,
                    type=dataset_data.get("datasetType", ""),
                    additional_info=dataset_data,
                )

                # Recursively parse nested datasets if present
                nested_datasets = dataset_data.get("datasets", [])
                if nested_datasets:
                    dataset.nested_datasets = self._parse_datasets(nested_datasets)

                datasets.append(dataset)

        return datasets

    def get_all_datasets(self, include_nested: bool = True) -> List[Dataset]:
        """
        Retrieve all datasets, optionally including nested datasets.

        :param include_nested: Whether to include nested datasets
        :return: Flattened list of datasets
        """

        def flatten_datasets(datasets: List[Dataset]) -> List[Dataset]:
            flattened = []
            for dataset in datasets:
                flattened.append(dataset)
                if include_nested:
                    flattened.extend(flatten_datasets(dataset.nested_datasets))
            return flattened

        return flatten_datasets(self.datasets)

    def find_dataset_by_name(self, name: str) -> Optional[Dataset]:
        """
        Find a dataset by name, searching through nested datasets.

        :param name: Name of the dataset to find
        :return: Matching dataset or None
        """

        def search_datasets(datasets: List[Dataset]) -> Optional[Dataset]:
            for dataset in datasets:
                if dataset.name == name:
                    return dataset
                # Recursively search nested datasets
                nested_result = search_datasets(dataset.nested_datasets)
                if nested_result:
                    return nested_result
            return None

        return search_datasets(self.datasets)

    def print_dataset_hierarchy(self, indent: int = 0):
        """
        Print a hierarchical view of datasets.

        :param indent: Current indentation level
        """

        def print_recursive(datasets: List[Dataset], current_indent: int):
            for dataset in datasets:
                logger.debug("  " * current_indent + f"{dataset.name} ({dataset.type})")
                if dataset.nested_datasets:
                    print_recursive(dataset.nested_datasets, current_indent + 1)

        print_recursive(self.datasets, indent)

    def get_domains_by_type(self, domain_type: str) -> List[Domain]:
        """
        Retrieve domains filtered by type.

        :param domain_type: Type of domain to filter (e.g., 'codedValue')
        :return: List of domains matching the type
        """
        return [domain for domain in self.domains if domain.type == domain_type]

    def get_datasets_by_type(self, dataset_type: str) -> List[Dataset]:
        """
        Retrieve datasets filtered by type.

        :param dataset_type: Type of dataset to filter (e.g., 'esriDTFeatureClass')
        :return: List of datasets matching the type
        """

        return [dataset for dataset in self.datasets if dataset.type == dataset_type]

    def generate_plantuml_diagram(self) -> str:
        """
        Generate a PlantUML diagram representation of the schema.

        :return: PlantUML diagram as a string
        """
        plantuml = ["@startuml", "skinparam classAttributeIconSize 0"]

        # Add domains
        for domain in self.domains:
            plantuml.append(f"class {domain.name} << (D,lightblue) Domain >> {{")
            for cv in domain.coded_values[:3]:  # Limit to first 3 for readability
                plantuml.append(f"  + {cv.name}: {cv.code}")
            if len(domain.coded_values) > 3:
                plantuml.append("  ... (more values)")
            plantuml.append("}")

        # Add datasets
        for dataset in self.datasets:
            plantuml.append(
                f"class {dataset.name} << ({dataset.type.lower()},{self._get_color(dataset.type)}) Dataset >> {{"
            )
            plantuml.append("}")

        plantuml.append("@enduml")
        return "\n".join(plantuml)

    def _get_color(self, dataset_type: str) -> str:
        """
        Assign colors to different dataset types.

        :param dataset_type: Type of dataset
        :return: Color name
        """
        color_map = {
            "esriDTFeatureClass": "#85BAA1",
            "esriDTRelationshipClass": "#544E61",
            "esriDTTable": "#9C92A9",
            "esriDTTopology": "purple",
        }
        return color_map.get(dataset_type, "gray")

    def compare_schemas(
        self, other_schema_manager: "ESRISchemaManager"
    ) -> Dict[str, Any]:
        """
        Compare this schema with another schema.

        :param other_schema_manager: Another ESRISchemaManager instance
        :return: Dictionary of differences
        """
        differences = {
            "domains": {"added": [], "removed": [], "modified": []},
            "datasets": {"added": [], "removed": [], "modified": []},
        }

        # Compare domains
        current_domain_names = {d.name for d in self.domains}
        other_domain_names = {d.name for d in other_schema_manager.domains}

        differences["domains"]["added"] = list(
            other_domain_names - current_domain_names
        )
        differences["domains"]["removed"] = list(
            current_domain_names - other_domain_names
        )

        # Compare datasets
        current_dataset_names = {d.name for d in self.datasets}
        other_dataset_names = {d.name for d in other_schema_manager.datasets}

        differences["datasets"]["added"] = list(
            other_dataset_names - current_dataset_names
        )
        differences["datasets"]["removed"] = list(
            current_dataset_names - other_dataset_names
        )

        return differences


def main():
    # Load schema
    schema_manager = ESRISchemaManager("ArcSDE/schema_report.json")

    # Get coded domains
    coded_domains = schema_manager.get_domains_by_type("codedValue")

    logger.info(coded_domains)

    all_datasets = schema_manager.get_all_datasets()

    # Find a specific dataset by name
    specific_dataset = schema_manager.find_dataset_by_name("MyDataset")

    # Print dataset hierarchy
    schema_manager.print_dataset_hierarchy()

    # Get feature classes
    feature_classes = schema_manager.get_datasets_by_type(
        "esriDTFeatureClass"
    )  # DEFeatureDataset  esriDTTopology
    for ds in schema_manager.datasets:
        if not ds.name.endswith("_I"):
            logger.info(f"{ds.name} - {ds.type}")

    # Generate PlantUML diagram
    plantuml_diagram = schema_manager.generate_plantuml_diagram()

    with open("test.puml", "w") as f:
        f.write(plantuml_diagram)

    # Compare with another schema
    # other_schema_manager = ESRISchemaManager('another_schema.json')
    # differences = schema_manager.compare_schemas(other_schema_manager)


if __name__ == "__main__":
    main()
