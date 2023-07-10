#!/usr/bin/python3
"""
contains method is_same_class
returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    use type() to check if obj is exactly an instance of a class
    returns True if the object is exactly an instance of the specified class
    """
    return type(obj) == a_class
