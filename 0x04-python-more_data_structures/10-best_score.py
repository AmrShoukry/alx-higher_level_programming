#!/usr/bin/python3
def best_score(a_dictionary):
    big = "None"
    big_int = None
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if big_int is None or value > big_int:
                big_int = value
                big = key
    return big
