#!/usr/bin/python3
import math


""" BEATIFUL BYTECODE """


class MagicClass:
    """ MagicClass with bytecode """
    def __init__(self, raidus=0):
        """ initiation of attributes """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ method area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ method circumference """
        return (2 * math.pi) * self.__radius