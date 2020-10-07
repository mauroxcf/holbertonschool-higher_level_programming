#!/usr/bin/python3
""" Base Geometry class """


class BaseGeometry:
    """
    adding area and integer validator
    """
    def area(self):
        """empty method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
