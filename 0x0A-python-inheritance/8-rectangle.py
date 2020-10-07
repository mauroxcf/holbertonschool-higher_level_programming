#!/usr/bin/python3
""" Base Geometry class """


class BaseGeometry:
    """
    adding area and integer validator
    """
    def integer_validator(self, name, value):
        """
        integer validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))

    def area(self):
        """empty method"""
        raise Exception("area() is not implemented")


class Rectangle(BaseGeometry):
    """ sub class rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
