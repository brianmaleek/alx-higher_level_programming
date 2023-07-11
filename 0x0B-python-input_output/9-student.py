#!/usr/bin/python3
"""
contains class Student
that initializes public instance attributes
first_name, last_name, age and has public method
to_json that retrieves a dictionary representation
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

    def to_json(self):
        """
        retrieves a dictionary representation
        """
        return self.__dict__
