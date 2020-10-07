#!/usr/bin/python3
"""
obtain a json string
"""


import json


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as jfile:
        object_json = json.load(jfile)
        return object_json
