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
class Field:
    name: str
    type: str
    is_nullable: bool
    length: Optional[int] = None
    precision: Optional[int] = None
    scale: Optional[int] = None
    required: bool = False
    editable: bool = True
    alias_name: Optional[str] = None
    model_name: Optional[str] = None
    domain: Optional[Domain] = None


@dataclass
class Dataset:
    """Represents a dataset in the ESRI SDE schema."""

    name: str
    type: str
    additional_info: Dict[str, Any] = field(default_factory=dict)
    nested_datasets: List["Dataset"] = field(default_factory=list)
    fields: List[Field] = field(default_factory=list)


class ESRISchemaManager:
    def __init__(self, schema_file_path: str):
        with open(schema_file_path, "r", encoding="utf-8") as file:
            self.schema = json.load(file)

        self.domains = self._parse_domains()
        self.datasets = self._parse_datasets(self.schema.get("datasets", []))

    def _parse_domain(self, domain_data: Dict[str, Any]) -> Domain:
        """
          Parse a single domain from domain data.

          :param domain_data: Dictionary containing domain information
          :return: Parsed Domain object
          "type": "codedValue",
        "name": "GC_LITHO_CD",
        "description": "GC_LITHO_CD",
        "codedValues": [
        "fieldType": "esriFieldTypeInteger",
        "mergePolicy": "esriMPTDefaultValue",
        "splitPolicy": "esriSPTDuplicate" }

         or
         "domainName": "GC_FOSS_LFOS_STATUS_CD",
                    "fieldType": "esriFieldTypeInteger",
                    "mergePolicy": "esriMPTDefaultValue",
                    "splitPolicy": "esriSPTDuplicate",
                    "description": "GC_FOSS_LFOS_STATUS_CD",
                    "codedValues": [
        """
        # Parse coded values
        if "domainName" in domain_data:
            type_ = "codedValue"
            domain_name = domain_data.get("domainName", "")

        else:
            type_ = domain_data.get("type", "")
            domain_name = domain_data.get("name", "")

        coded_values = [
            CodedValue(name=cv.get("name", ""), code=cv.get("code"))
            for cv in domain_data.get("codedValues", [])
        ]

        return Domain(
            type=type_,
            name=domain_name,
            description=domain_data.get("description", ""),
            coded_values=coded_values,
        )

    def _parse_domains(self) -> List[Domain]:
        """
        Parse all domains from the schema.

        :return: List of Domain objects
        """
        return [
            self._parse_domain(domain_data)
            for domain_data in self.schema.get("domains", [])
        ]

    def _parse_fields(self, fields_data: Dict[str, Any]) -> List[Field]:
        """
        Parse fields from dataset, including domain references.

        :param fields_data: Fields data from the dataset
        :return: List of parsed Field objects
        """
        fields = []
        for field_data in fields_data.get("fieldArray", []):
            # Check if field has a domain reference
            domain = None
            domain_name = field_data.get("domain")
            if domain_name and self._find_domain_by_name(domain_name) is None:
                # domain = self._find_domain_by_name(domain_name)
                if "domain" in field_data:
                    domain = self._parse_domain(field_data["domain"])

                    self.domains.append(domain)

            field = Field(
                name=field_data.get("name", ""),
                type=field_data.get("type", ""),
                is_nullable=field_data.get("isNullable", True),
                length=field_data.get("length"),
                precision=field_data.get("precision"),
                scale=field_data.get("scale"),
                required=field_data.get("required", False),
                editable=field_data.get("editable", True),
                alias_name=field_data.get("aliasName"),
                model_name=field_data.get("modelName"),
                domain=domain,
            )
            fields.append(field)

        return fields

    def _parse_datasets(self, dataset_list: List[Dict[str, Any]]) -> List[Dataset]:
        datasets = []
        for dataset_data in dataset_list:
            # Create current dataset
            dataset_name = dataset_data.get("name", "")
            if dataset_name.startswith(
                (
                    "TOPGIS_GC",
                    "GC_",
                )
            ):
                if not dataset_name.endswith("_I"):
                    dataset = Dataset(
                        name=dataset_name,
                        type=dataset_data.get("datasetType", ""),
                        additional_info=dataset_data,
                    )

                    # Parse fields if present
                    if "fields" in dataset_data:
                        dataset.fields = self._parse_fields(dataset_data["fields"])

                    # Recursively parse nested datasets if present
                    nested_datasets = dataset_data.get("datasets", [])
                    if nested_datasets:
                        dataset.nested_datasets = self._parse_datasets(nested_datasets)

                    datasets.append(dataset)

        return datasets

    def _find_domain_by_name(self, domain_name: str) -> Optional[Domain]:
        """
        Find a domain by its name.

        :param domain_name: Name of the domain to find
        :return: Matching domain or None
        """
        return next(
            (domain for domain in self.domains if domain.name == domain_name), None
        )

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

    def get_fields_by_type(self, field_type: str) -> List[Field]:
        """
        Find all fields of a specific type across all datasets.

        :param field_type: Type of field to search for
        :return: List of fields matching the type
        """

        def find_fields_by_type(datasets: List[Dataset]) -> List[Field]:
            matching_fields = []
            for dataset in datasets:
                # Find fields matching type in current dataset
                matching_fields.extend(
                    [field for field in dataset.fields if field.type == field_type]
                )

                # Recursively search nested datasets
                matching_fields.extend(find_fields_by_type(dataset.nested_datasets))

            return matching_fields

        return find_fields_by_type(self.datasets)

    def generate_field_summary(self) -> Dict[str, int]:
        """
        Generate a summary of field types across all datasets.

        :return: Dictionary of field type counts
        """
        field_type_summary = {}
        for field in self.get_all_fields():
            field_type_summary[field.type] = field_type_summary.get(field.type, 0) + 1
        return field_type_summary

    def get_all_fields(self) -> List[Field]:
        """
        Retrieve all fields from all datasets.

        :return: Flattened list of all fields
        """

        def collect_fields(datasets: List[Dataset]) -> List[Field]:
            all_fields = []
            for dataset in datasets:
                all_fields.extend(dataset.fields)
                # Recursively collect fields from nested datasets
                all_fields.extend(collect_fields(dataset.nested_datasets))
            return all_fields

        return collect_fields(self.datasets)

    def get_datasets_with_domain(self, domain_name: str) -> List[Dataset]:
        """
        Find datasets that have fields with a specific domain.

        :param domain_name: Name of the domain to search for
        :return: List of datasets with fields using the domain
        """

        def find_datasets_with_domain(datasets: List[Dataset]) -> List[Dataset]:
            matching_datasets = []
            for dataset in datasets:
                # Check if any field uses the domain
                if any(
                    field.domain and field.domain.name == domain_name
                    for field in dataset.fields
                ):
                    matching_datasets.append(dataset)

                # Recursively check nested datasets
                matching_datasets.extend(
                    find_datasets_with_domain(dataset.nested_datasets)
                )

            return matching_datasets

        return find_datasets_with_domain(self.datasets)

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

    def print_domain_field_relationships(self):
        """
        Print relationships between domains and the fields that use them.
        """
        for domain in self.domains:
            print(f"\nDomain: {domain.name}")
            matching_datasets = self.get_datasets_with_domain(domain.name)

            if matching_datasets:
                print("  Used in datasets:")
                for dataset in matching_datasets:
                    print(f"    - {dataset.name}")
                    # Find and print specific fields using this domain
                    domain_fields = [
                        f.name
                        for f in dataset.fields
                        if f.domain and f.domain.name == domain.name
                    ]
                    for field_name in domain_fields:
                        print(f"      * {field_name}")
            else:
                print("  Not used in any datasets")

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

    # Print domain and field relationships
    # schema_manager.print_domain_field_relationships()

    # Generate PlantUML diagram
    plantuml_diagram = schema_manager.generate_plantuml_diagram()

    with open("test.puml", "w") as f:
        f.write(plantuml_diagram)

    # Compare with another schema
    # other_schema_manager = ESRISchemaManager('another_schema.json')
    # differences = schema_manager.compare_schemas(other_schema_manager)

    for cd in schema_manager.domains:
        logger.info(cd.name)

    print(schema_manager._find_domain_by_name("GC_PNT_HCON_EPOCH_CD__"))


if __name__ == "__main__":
    main()
