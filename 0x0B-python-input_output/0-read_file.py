#!/usr/bin/python3
""" read a file """


def read_file(filename=""):
    """
    read and print a file
    """
    with open(filename, "r") as reader:
        print(reader.read())
