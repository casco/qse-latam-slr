import pandas as pd

RELEVANT_KEYS = ['author', 'year', 'title']


def entry_as_flat_dict(entry):
    result = {}
    fields = entry.fields_dict
    for (key, field) in fields.items():
        if key in RELEVANT_KEYS:
            result.update({key: field.value})
    return result


def df_from_library(library):
    return pd.DataFrame.from_records(list(map(entry_as_flat_dict, library.entries)))
