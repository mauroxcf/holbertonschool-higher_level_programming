#!/usr/bin/python3
"""
obtain a json string
"""


import json


def save_to_json_file(my_obj, filename):
    """
    write object json to a file
    """
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(my_obj))
