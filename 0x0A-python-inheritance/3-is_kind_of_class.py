#!/usr/bin/python3
""" isinstance """


def is_kind_of_class(obj, a_class):
    """
    verify its if a instance
    return true or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
