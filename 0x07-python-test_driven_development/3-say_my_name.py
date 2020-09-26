#!/usr/bin/python3
""" Program that print the first and last name """


def say_my_name(first_name, last_name=""):
    """
    the first and last name must be strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
