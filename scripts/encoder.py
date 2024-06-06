import json
import yaml


from schema import GeocoverSchema


class CustomEncoder:
    def __init__(self):
        pass

    def to_serializable_dict(self, obj):
        if isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        elif isinstance(obj, (list, tuple, set)):
            return [self.to_serializable_dict(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self.to_serializable_dict(value) for key, value in obj.items()}
        else:
            # If it's a custom object, convert it to a dictionary
            if hasattr(obj, "__dict__"):
                return {
                    key: self.to_serializable_dict(value)
                    for key, value in obj.__dict__.items()
                }
            else:
                return str(obj)  # Fallback: convert to string

    def to_json(self, obj, **kwargs):
        serializable_dict = self.to_serializable_dict(obj)
        return json.dumps(serializable_dict, **kwargs)

    def to_yaml(self, obj, **kwargs):
        serializable_dict = self.to_serializable_dict(obj)
        return yaml.dump(serializable_dict, **kwargs)


class ExtendedEncoder(CustomEncoder):
    def to_serializable_dict(self, obj):
        # Handle specific object types here
        if obj.__class__.__name__ == "Workspace Domain object":
            return self._serialize_coded_domain(obj)
        elif isinstance(obj, Subtype):
            return self._serialize_subtype(obj)
        elif isinstance(obj, Table):
            return self._serialize_table(obj)
        elif isinstance(obj, FeatureClass):
            return self._serialize_feature_class(obj)
        elif isinstance(obj, GeocoverSchema):
            return self._serialize_database_schema(obj)
        else:
            # Fallback to the base class implementation
            return super().to_serializable_dict(obj)

    def _serialize_coded_domain(self, obj):
        dom_dict = {}

        dom_dict[obj.name] = {"type": obj.domainType}
        if obj.domainType == "CodedValue":
            dom_dict[obj.name]["codedValues"] = obj.codedValues

        elif obj.domainType == "Range":
            dom_dict[obj.name]["range"] = obj.range

        return dom_dict

    def _serialize_subtype(self, obj):
        return {"name": obj.name, "fields": obj.fields}

    def _serialize_table(self, obj):
        return {
            "name": obj.name,
            "columns": [
                {"name": field.name, "type": field.type} for field in obj.columns
            ],
        }

    def _serialize_feature_class(self, obj):
        return {
            "name": obj.name,
            "columns": [
                {"name": field.name, "type": field.type} for field in obj.columns
            ],
            "subtypes": obj.subtypes,
            "coded_domains": obj.coded_domains,
        }

    def _serialize_database_schema(self, obj):
        return {
            "tables": [self.to_serializable_dict(table) for table in obj.tables],
            "feature_classes": [
                self.to_serializable_dict(fc) for fc in obj.feature_classes
            ],
            "coded_domains": [
                self.to_serializable_dict(cd) for cd in obj.coded_domains
            ],
        }


# Example custom classes
class CodedDomain:
    def __init__(self, name, domain_type, coded_values):
        self.name = name
        self.domain_type = domain_type
        self.coded_values = coded_values


class Subtype:
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields


class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns


class FeatureClass(Table):
    def __init__(self, name, columns, subtypes, coded_domains):
        super().__init__(name, columns)
        self.subtypes = subtypes
        self.coded_domains = coded_domains


"""
# Example usage
coded_domain = CodedDomain("ExampleDomain", "CodedValue", {1: "One", 2: "Two"})
subtype = Subtype("Subtype1", ["Field1", "Field2"])
table = Table("Table1", ["Column1", "Column2"])
feature_class = FeatureClass("FeatureClass1", ["Column1", "Column2"], [subtype], [coded_domain])

encoder = ExtendedEncoder()
json_output = encoder.to_json(feature_class, indent=4)
yaml_output = encoder.to_yaml(feature_class, default_flow_style=False)

print("JSON Output:")
print(json_output)
print("\nYAML Output:")
print(yaml_output)

"""
