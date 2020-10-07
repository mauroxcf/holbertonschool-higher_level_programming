#!/usr/bin/python3
"""
obtain a json string
"""


import json


def to_json_string(my_obj):
    """
    read the json object into a string
    """
    json_obj = json.dumps(my_obj)
    return json_obj
