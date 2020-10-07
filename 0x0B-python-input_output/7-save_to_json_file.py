#!/usr/bin/python3
import json


"""
save in to json file
"""


def save_to_json_file(my_obj, filename):
    """
    write object json to a file
    """
    with open(filename, "w") as json_file:
        json_file.write(json.dumps(my_obj))
