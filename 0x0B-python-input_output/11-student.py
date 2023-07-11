#!/usr/bin/python3
"""
contains the class Student
initiates public instance attributes first_name, last_name, age
and has public method to_json that retrieves a dictionary representation
"""


class Student:
    """
    public Attributes:
        first_name
        last_name
        age
    Public method:
        to_json: retrieves a dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization of public attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        Returns:
            only return attributes contained in attrs
            Return all attributes if attrs is None
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attribute in attrs:
                if attribute in self.__dict__.keys():
                    new_dict[attribute] = self.__dict__[attribute]
            return new_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
