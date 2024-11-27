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
    # domain: Optional[Domain] = None
    domain: Optional[str] = None


@dataclass
class Dataset:
    """Represents a dataset in the ESRI SDE schema."""

    name: str
    type: str
    additional_info: Dict[str, Any] = field(default_factory=dict)
    nested_datasets: List["Dataset"] = field(default_factory=list)
    fields: List[Field] = field(default_factory=list)


@dataclass
class RelationshipClassKey:
    """Represents a key in a relationship class."""

    dataset_type: str
    object_key_name: str
    class_key_name: str = ""
    key_role: str = ""


@dataclass
class RelationshipClass:
    """Represents a relationship class in the ESRI SDE schema."""

    catalog_path: str
    name: str
    dataset_type: str

    # Relationship properties
    cardinality: str
    notification: str
    is_attributed: bool
    is_composite: bool
    is_reflexive: bool

    # Class names
    origin_class_names: List[str]
    destination_class_names: List[str]

    # Path labels
    forward_path_label: Optional[str] = None
    backward_path_label: Optional[str] = None

    # Keys
    origin_class_keys: List[RelationshipClassKey] = field(default_factory=list)
    destination_class_keys: List[RelationshipClassKey] = field(default_factory=list)

    # Fields (reusing the Field class from previous implementation)
    fields: List[Field] = field(default_factory=list)

    # Additional metadata
    children_expanded: bool = False
    raster_field_name: str = ""
    extension_properties: Optional[Dict[str, Any]] = None


def is_geocover(name):
    if name.startswith(
        (
            "TOPGIS_GC",
            "GC_",
        )
    ) and not name.endswith("_I"):
        return True
    return False


class ESRISchemaManager:
    def __init__(self, schema_file_path: str):
        with open(schema_file_path, "r", encoding="utf-8") as file:
            self.schema = json.load(file)

        self.domains = self._parse_domains()
        self.datasets = self._parse_datasets(self.schema.get("datasets", []))

        self.relationship_classes = self._parse_relationship_classes()

    def _parse_relationship_class_keys(
        self, keys_data: List[Dict[str, Any]]
    ) -> List[RelationshipClassKey]:
        """
        Parse relationship class keys.

        :param keys_data: List of key data dictionaries
        :return: List of RelationshipClassKey objects
        """
        return [
            RelationshipClassKey(
                dataset_type=key.get("datasetType", ""),
                object_key_name=key.get("objectKeyName", ""),
                class_key_name=key.get("classKeyName", ""),
                key_role=key.get("keyRole", ""),
            )
            for key in keys_data
        ]

    def _parse_relationship_classes(self) -> List[RelationshipClass]:
        """
        Parse relationship classes from the schema.

        :return: List of RelationshipClass objects
        """
        relationship_classes = []

        # Extract relationship classes from datasets
        def extract_relationship_classes(
            datasets: List[Dict[str, Any]],
        ) -> List[Dict[str, Any]]:
            rels = []
            for dataset in datasets:
                if dataset.get("datasetType") == "esriDTRelationshipClass":
                    rels.append(dataset)
                # Recursively check nested datasets
                if "datasets" in dataset:
                    rels.extend(extract_relationship_classes(dataset["datasets"]))
            return rels

        # Get relationship classes from the schema
        rel_class_data = extract_relationship_classes(self.schema.get("datasets", []))

        for rc in rel_class_data:
            # Parse fields (reusing the method from previous implementation)
            fields = self._parse_fields(rc.get("fields", {})) if "fields" in rc else []

            # Extract origin and destination class names
            origin_classes = [
                cls.get("name", "") for cls in rc.get("originClassNames", [])
            ]
            destination_classes = [
                cls.get("name", "") for cls in rc.get("destinationClassNames", [])
            ]

            relationship_class = RelationshipClass(
                catalog_path=rc.get("catalogPath", ""),
                name=rc.get("name", ""),
                dataset_type=rc.get("datasetType", ""),
                # Relationship properties
                cardinality=rc.get("cardinality", ""),
                notification=rc.get("notification", ""),
                is_attributed=rc.get("isAttributed", False),
                is_composite=rc.get("isComposite", False),
                is_reflexive=rc.get("isReflexive", False),
                # Class names
                origin_class_names=origin_classes,
                destination_class_names=destination_classes,
                # Path labels
                forward_path_label=rc.get("forwardPathLabel"),
                backward_path_label=rc.get("backwardPathLabel"),
                # Keys
                origin_class_keys=self._parse_relationship_class_keys(
                    rc.get("originClassKeys", [])
                ),
                destination_class_keys=self._parse_relationship_class_keys(
                    rc.get("destinationClassKeys", [])
                ),
                # Fields
                fields=fields,
                # Additional metadata
                children_expanded=rc.get("childrenExpanded", False),
                raster_field_name=rc.get("rasterFieldName", ""),
                extension_properties=rc.get("extensionProperties"),
            )

            relationship_classes.append(relationship_class)

        return relationship_classes

    def find_relationship_classes(
        self,
        origin_class: Optional[str] = None,
        destination_class: Optional[str] = None,
    ) -> List[RelationshipClass]:
        """
        Find relationship classes based on origin or destination classes.

        :param origin_class: Name of the origin class to filter by
        :param destination_class: Name of the destination class to filter by
        :return: List of matching RelationshipClass objects
        """
        return [
            rc
            for rc in self.relationship_classes
            if (not origin_class or origin_class in rc.origin_class_names)
            and (
                not destination_class or destination_class in rc.destination_class_names
            )
        ]

    def get_relationship_class_by_name(self, name: str) -> Optional[RelationshipClass]:
        """
        Find a relationship class by its full name.

        :param name: Full name of the relationship class
        :return: RelationshipClass object or None if not found
        """
        return next((rc for rc in self.relationship_classes if rc.name == name), None)

    def summarize_relationship_classes(self) -> Dict[str, Any]:
        """
        Generate a summary of relationship classes.

        :return: Dictionary with relationship class summary
        """
        return {
            "total_count": len(self.relationship_classes),
            "cardinality_distribution": self._count_by_attribute("cardinality"),
            "attributed_count": sum(
                1 for rc in self.relationship_classes if rc.is_attributed
            ),
            "composite_count": sum(
                1 for rc in self.relationship_classes if rc.is_composite
            ),
            "reflexive_count": sum(
                1 for rc in self.relationship_classes if rc.is_reflexive
            ),
        }

    def _count_by_attribute(self, attribute: str) -> Dict[str, int]:
        """
        Count occurrences of a specific attribute across relationship classes.

        :param attribute: Name of the attribute to count
        :return: Dictionary of attribute value counts
        """
        counts = {}
        for rc in self.relationship_classes:
            value = getattr(rc, attribute, None)
            counts[value] = counts.get(value, 0) + 1
        return counts

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
        try:
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
        except (KeyError, ValueError, TypeError) as e:
            logger.warning(f"Error parsing domain data: {e}. Data: {domain_data}")
            return None

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
            domain_name = None
            domain_data = field_data.get("domain")
            if domain_data:
                domain = self._parse_domain(domain_data)

                if (
                    domain is not None
                    and self._find_domain_by_name(domain.name) is None
                ):
                    domain_name = domain.name
                    logger.info(domain_name)
                    if is_geocover(domain_name):
                        self.domains.append(domain)
                else:
                    logger.info(domain_data)

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
                domain=domain_name,
            )
            fields.append(field)

        return fields

    def _parse_datasets(self, dataset_list: List[Dict[str, Any]]) -> List[Dataset]:
        datasets = []
        for dataset_data in dataset_list:
            # Create current dataset
            dataset_name = dataset_data.get("name", "")
            if is_geocover(dataset_name):
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
        logger.info(f"Domain={cd.name}")
    logger.info(f"Number of domains: {len(schema_manager.domains)}")

    logger.info(schema_manager._find_domain_by_name("GC_PNT_HCON_EPOCH_CD"))
    logger.info(schema_manager._find_domain_by_name("GC_CORRECTION_STATE_CD"))

    bedrock_relationships = schema_manager.find_relationship_classes(
        origin_class="TOPGIS_GC.GC_BEDROCK"
    )
    logger.info(bedrock_relationships)

    # Get a specific relationship class
    specific_relationship = schema_manager.get_relationship_class_by_name(
        "TOPGIS_GC.GC_BEDR_LITHO_GC_LITHO_BED"
    )
    logger.info(specific_relationship)

    # Get summary of relationship classes
    relationship_summary = schema_manager.summarize_relationship_classes()
    logger.info(relationship_summary)
    
    for relationship in schema_manager.relationship_classes:
        logger.info(relationship.name)


if __name__ == "__main__":
    main()