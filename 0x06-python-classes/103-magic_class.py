#!/usr/bin/python3


""" BEATIFUL BYTECODE """


import math


class MagicClass:
    """ MagicClass with bytecode """
    def __init__(self, radius):
        """ initiation of attributes """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ method area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ method circumference """
        return (2 * math.pi) * self.__radius
