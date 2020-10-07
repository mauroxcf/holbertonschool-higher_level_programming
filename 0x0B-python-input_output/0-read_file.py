#!/usr/bin/python3
def read_file(filename=""):
    """
    read and print a file
    """
    with open(filename) as reader:
        print(reader.read())
