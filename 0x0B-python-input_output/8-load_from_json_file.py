#!/user/bin/python3
import json


"""
load from a json file
"""


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as jfile:
        object_json = json.load(jfile)
        return object_json
