#!/usr/bin/python3
""" read lines """


def read_lines(filename="", nb_lines=0):
    """
    open a read a file
    """
    with open(filename, mode='r', encoding="utf-8") as reader:
        count = 0
        for line in reader:
            print(line, end="")
            count += 1
            if count == nb_lines:
                break
