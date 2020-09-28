#!/usr/bin/python3
""" rectangle having width and height """


class Rectangle:
    """
    adding the area and perimetrer
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ area calculation """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter calculation """
        widthpmt, heightpmt = self.__width, self.__height
        if widthpmt is 0 or heightpmt is 0:
            return 0

        return (widthpmt * 2) + (heightpmt * 2)
