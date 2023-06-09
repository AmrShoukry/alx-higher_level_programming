#!/usr/bin/python3
""" Model """

import json


def load_from_json_file(filename):
    """ Function """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
