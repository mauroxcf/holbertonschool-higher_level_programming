#!/usr/bin/python3
""" Program that prints a square """


def print_square(size):
    """
    size of the square must be a integer
    """
    if type(size) is int:
        size = int(size)
    else:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
