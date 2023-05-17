#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return a_dictionary
    keys = []
    for a_key, a_value in a_dictionary.items():
        if a_value == value:
            keys.append(a_key)
    for key in keys:
        a_dictionary.pop(key)
    return a_dictionary
