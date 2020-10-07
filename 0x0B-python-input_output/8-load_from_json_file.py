#!/usr/bin/python3
"""
obtain a json string
"""


import json


def load_from_json_file(filename):
    """
    load from json
    """
    with open(filename, mode="r") as jfile:
        object_json = json.load(jfile)
        return object_json
