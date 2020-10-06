#!/usr/bin/python3
""" subclass """


def inherits_from(obj, a_class):
    """
    issubclass  the type of the object
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
