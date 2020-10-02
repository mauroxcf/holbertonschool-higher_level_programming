#!/usr/bin/python3
""" program that make a identation with certain characters"""


def text_indentation(text):
    """
    text is a lecture that must be separated with line jump
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    aux = 0
    new_string = ""
    for i in text:
        if aux is 0:
            if i is " ":
                continue
            else:
                aux = 1
        if i is "." or i is "?" or i is ":":
            aux = 0
            i += "\n" * 2
            print(i, end="")
        else:
            print(i, end="")
