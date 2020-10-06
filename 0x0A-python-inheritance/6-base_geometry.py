#!/usr/bin/python3
""" Empty class """

class BaseGeometry:
    """
    base geometry class
    """
    def area(self):
        if self:
            raise Exception("area() is not implemented")
