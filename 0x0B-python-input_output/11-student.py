#!/usr/bin/python3
""" Class Student """


class Student:
    """
    Student info
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        class object type
        """
        return self.__dict__

