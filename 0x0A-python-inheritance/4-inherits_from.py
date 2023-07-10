#!/usr/bin/python3
"""
defines an inherited class
"""


def inherits_from(obj, a_class):
    """
    use issubclass() to check if obj is an instance of a_class
    that inherited from the specified class
    Returns:
        True if the object is an instance of a_class
        False if the object is not an instance of a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
