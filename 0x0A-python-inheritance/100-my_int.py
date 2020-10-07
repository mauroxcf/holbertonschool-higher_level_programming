#!/usr/bin/python3
""" MyInt class rebel """


class MyInt(int):
    """ Rebel """
    def __init__(self, value=0):
        """ Constructor """
        self.__value = value

    def __eq__(self, value):
        """ invert equal """
        return not (self.__value == value)

    def __ne__(self, value):
        """ invert negation """
        return not (self.__value != value)
