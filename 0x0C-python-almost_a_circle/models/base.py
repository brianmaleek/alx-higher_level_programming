#!/usr/bin/python3
"""
Module Base class
contains:
    class Base
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)
"""


import json


class Base():
    """
    Define: Class Base
    attributes:
        __nb_objects: private class attribute
    methods:
        __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method
        Attributes:
            id: public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of list_objs to a file
        """
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
