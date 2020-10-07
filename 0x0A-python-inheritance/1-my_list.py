#!/usr/bin/python3
""" Class my list """


class MyList(list):
    """
    inherit class
    """
    def print_sorted(self):
        print(sorted(self))
