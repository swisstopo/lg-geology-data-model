import logging


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
