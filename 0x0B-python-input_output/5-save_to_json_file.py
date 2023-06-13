#!/usr/bin/python3
""" Model """

import json


def save_to_json_file(my_obj, filename):
    """ Function """
    return json.dump(my_obj, filename)
