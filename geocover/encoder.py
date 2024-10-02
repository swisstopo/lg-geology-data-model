import json
import yaml
import datetime

from . import schema


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
        elif isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        # Panda DataFrame
        elif hasattr(obj, "to_dict"):
            return obj.to_dict(orient="records")
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
        if hasattr(obj, "originClassNames"):
            return self._serialize_relationship_desc(obj)

        elif obj.__class__.__name__ == "Workspace Domain object":
            return self._serialize_coded_domain(obj)

        elif isinstance(obj, schema.GeocoverSchema):
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

    def _serialize_relationship_desc(self, obj):
        oriClasses = obj.originClassNames

        dest_keys = []
        if len(obj.destinationClassKeys) > 0:
            for key in obj.destinationClassKeys:
                key_name, key_role, _ = key
                dest_keys.append({"name": key_name, "role": key_role})
        orig_keys = []
        if len(obj.originClassKeys) > 0:
            for key in obj.originClassKeys:
                key_name, key_role, _ = key
                orig_keys.append({"name": key_name, "role": key_role})

        return {
            "origin": oriClasses,  # oriClass,
            "destination": obj.destinationClassNames[0],
            "forwardPathLabel": obj.forwardPathLabel,
            "backwardPathLabel": obj.backwardPathLabel,
            "isAttachmentRelationship": obj.isAttachmentRelationship,
            "cardinality": obj.cardinality,
            "originClassKeys": orig_keys,
            "destinationClassKeys": dest_keys,
            "is_attributed": obj.isAttributed,
            "is_composite": obj.isComposite,
            "is_reflexive": obj.isReflexive,
            "classKey": obj.classKey,
            "keyType": obj.keyType,
        }
