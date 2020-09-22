#!/usr/bin/python3


""" Square Estructure"""


class Square:
    """ Class represent a square """
    def __init__(self, size=0):
        """ condition to evaluate if size its a negative or a int attribute """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
