#!/usr/bin/python3
"""
contains method inherits_from
returns True if the object is an instance of a class that inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """
    use issubclass() to check if obj is an instance of a class
    that inherited from the specified class
    Returns:
        True if the object is an instance of a#-class
        False if the object is not an instance of a_class
    """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
