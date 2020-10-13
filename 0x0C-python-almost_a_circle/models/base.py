#!/usr/bin/python3
""" Base class """

import json
import os


class Base:
    """ First class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            list_dictionaries = []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        """
        new_obj = []
        filename = cls.__name__ + ".json"

        if list_objs is not None:
            for i in list_objs:
                new_obj.append(cls.to_dictionary(i))

        with open(filename, mode="w", encoding="utf-8") as newfile:
            newfile.write(cls.to_json_string(new_obj))

    @staticmethod
    def from_json_string(json_string):
        """ list of the JSON string representation """
        json_list = []
        if not json_string:
            return json_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy_SR = cls(2, 3)

        if cls.__name__ == "Square":
            dummy_SR = cls(1, 2)

        dummy_SR.update(**dictionary)
        return dummy_SR

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        new_instance = []
        filename = cls.__name__ + ".json"

        if not os.path.isfile(filename):
            return new_instance

        with open(filename, mode="r", encoding="utf-8") as newfile:
            new_instance = cls.from_json_string(newfile.read())
        return [cls.create(**dic) for dic in new_instance]
