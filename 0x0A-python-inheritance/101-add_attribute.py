#!/usr/bin/python3
"""Adding a atribute"""


def add_attribute(obj, name, value):
    """Add or update and atrribute of an object"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
