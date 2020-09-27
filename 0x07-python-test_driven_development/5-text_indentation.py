#!/usr/bin/python3
""" program that make a identation with certain characters"""


def text_indentation(text):
    """
    text is a lecture that must be separated with line jump
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i is "." or i is "?" or i is ":":
            i += "\n"
        print(i, end="")
