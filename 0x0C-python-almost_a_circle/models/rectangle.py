#!/usr/bin/python3
""" rectangle class """


from models.base import Base

class Rectangle(Base):
    """ rectangle with weight and height """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ inicialization of instance attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """ rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ got the value height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ got the value width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """ rectangle x """
        return self.__x

    @x.setter
    def x(self, value):
        """ got the value x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ rectangle y """
        return self.__y

    @y.setter
    def y(self, value):
        """ got the value y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ prints the rectangle """
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        """ return info about the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        compare = ["id", "width", "height", "x", "y"]
        if args and args is not None:
            for i in range(len(args)):
                setattr(self, compare[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
