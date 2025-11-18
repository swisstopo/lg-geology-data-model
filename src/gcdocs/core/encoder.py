import json
import yaml
import datetime


class CustomEncoder:
    @classmethod
    def _to_serializable_dict(cls, obj):
        if isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        elif isinstance(obj, (list, tuple, set)):
            return [cls._to_serializable_dict(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: cls._to_serializable_dict(value) for key, value in obj.items()}
        elif isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        elif hasattr(obj, "to_dict"):
            return obj.to_dict(orient="records")
        elif hasattr(obj, "__dict__"):
            return {
                key: cls._to_serializable_dict(value)
                for key, value in obj.__dict__.items()
            }
        else:
            return str(obj)

    @classmethod
    def to_json(cls, obj, **kwargs):
        return json.dumps(cls._to_serializable_dict(obj), **kwargs)

    @classmethod
    def to_yaml(cls, obj, **kwargs):
        return yaml.dump(cls._to_serializable_dict(obj), **kwargs)
