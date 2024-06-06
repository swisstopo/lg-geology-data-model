import os
import json
import logging
import pandas as pd
import arcpy


def arcgis_table_to_df(in_fc, input_fields=None, query=""):
    """Function will convert an arcgis table into a pandas dataframe with an object ID index, and the selected
    input fields using an arcpy.da.SearchCursor.
    :param - in_fc - input feature class or table to convert
    :param - input_fields - fields to input to a da search cursor for retrieval
    :param - query - sql query to grab appropriate values
    :returns - pandas.DataFrame"""
    OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
    available_fields = [field.name for field in arcpy.ListFields(in_fc)]
    logging.debug(available_fields)
    logging.debug(input_fields)
    if input_fields:
        final_fields = list(set([OIDFieldName] + input_fields) & set(available_fields))
    else:
        final_fields = available_fields
    logging.debug("Intersection:", final_fields)
    data = [
        row for row in arcpy.da.SearchCursor(in_fc, final_fields, where_clause=query)
    ]
    fc_dataframe = pd.DataFrame(data, columns=final_fields)
    fc_dataframe = fc_dataframe.set_index(OIDFieldName, drop=True)
    return fc_dataframe


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
