import os
import json
import logging


def dump_dict_to_json(data, file_path):
    """
    Dumps a Python dictionary to a JSON file.

    Args:
        data (dict): The dictionary to be dumped.
        file_path (str): The path (including the file name) where the JSON file will be saved.

    Raises:
        TypeError: If data is not a dictionary.
        ValueError: If the file path is invalid.
        IOError: If there is an error writing to the file.
    """

    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")

    # Ensure the directory exists
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            raise ValueError(f"Invalid file path: {e}")

    try:
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
    except IOError as e:
        raise IOError(f"Error writing to file: {e}")


def merge_two_dicts(x, y):
    """Given two dictionaries, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


def get_field_type(stdict):
    field_type_dict = {}
    for stkey in list(stdict.keys()):
        if stkey == "FieldValues":
            fields = stdict[stkey]
            for field, fieldvals in list(fields.items()):
                if not fieldvals[1] is None:
                    logging.debug(f"   {field}: {fieldvals[1].name} {fieldvals[0]}")
                    field_type_dict[field] = fieldvals[1].name
    return field_type_dict
