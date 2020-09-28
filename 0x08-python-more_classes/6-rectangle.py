#!/usr/bin/python3
""" rectangle having width and height """


class Rectangle:
    """
    counting the number of instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ instantiation of instance attributes """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ set the height value """
        return self.__height

    @height.setter
    def height(self, value):
        """ got the height value """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ set the width value """
        return self.__width

    @width.setter
    def width(self, value):
        """ got the width value """
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

    def __str__(self):
        """ print the rectangle """
        if self.__width is 0 or self.__height is 0:
            return ""
        rect_print = "#" * self.__width + "\n"
        rect_print = rect_print * self.__height
        rect_print = rect_print[:-1]
        return rect_print

    def __repr__(self):
        """ represent the width and height of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ delete instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
