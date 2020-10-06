#!/usr/bin/python3
""" Base Geometry class """

class BaseGeometry:
    """
    adding area and integer validator
    """
    def area(self):
        if self:
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ sub class rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ area calculation """
        return self.__width * self.__height

    def __str__(self):
        """ print the object string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
