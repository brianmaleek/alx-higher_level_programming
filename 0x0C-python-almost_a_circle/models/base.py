#!/usr/bin/python3
"""
Module Base class
contains:
    class Base
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)
"""


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
