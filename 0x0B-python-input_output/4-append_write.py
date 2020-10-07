#!/usr/bin/python3
""" append in a file """


def append_write(filename="", text=""):
    """
    adding a new text info
    """
    with open(filename, mode='a+', encoding="utf-8") as newtext:
        return newtext.write(text)
