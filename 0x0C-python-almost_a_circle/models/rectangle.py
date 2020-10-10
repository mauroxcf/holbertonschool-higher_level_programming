#!/usr/bin/python3
""" rectangle class """


from models.base import Base

class Rectangle(Base):
    """ rectangle with weight and height """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ inicialization of instance attributes """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ got the value width """
        self.__width = value

    @property
    def height(self):
        """ rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ got the value height """
        self.__height = value

    @property
    def x(self):
        """ rectangle x """
        return self.__x

    @x.setter
    def x(self, value):
        """ got the value x """
        self.__x = value

    @property
    def y(self):
        """ rectangle y """
        return self.__y

    @y.setter
    def y(self, value):
        """ got the value y """
        self.__y = value
