#!/usr/bin/python3
""" Base Geometry class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        constructor in square class and using area method
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area calculation """
        return self.__size * self.__size
