#!/usr/bin/python3
""" Model """

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('load_from_json_file').load_from_json_file

args = []

for arg in sys.argv:
    args.append(arg)

save_to_json_file(args, "add_item.json")
load_from_json_file("add_item.json")