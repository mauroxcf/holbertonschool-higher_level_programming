#!/usr/bin/python3
""" verify the type of the class """


def is_same_class(obj, a_class):
    """
    funcion return true or false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
