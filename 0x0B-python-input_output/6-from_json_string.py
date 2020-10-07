#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    using json.loads to read the json object
    """
    json_obj = json.loads(my_str)
    return json_obj
