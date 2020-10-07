#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, "r") as reader:
        return len(reader.readlines())
