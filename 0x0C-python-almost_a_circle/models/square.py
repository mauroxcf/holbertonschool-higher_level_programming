#!/usr/bin/python3
""" rectangle class """


from models.rectangle import Rectangle

class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ inicialization of instance attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Square size """
        return self.width

    @size.setter
    def size(self, value):
        """ Square size """
        self.width = value
        self.height = value

    def __str__(self):
        """ return info about the rectangle """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        compare = ["id", "size", "x", "y"]
        if args and args is not None:
            for i in range(len(args)):
                setattr(self, compare[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        dicto = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dicto
