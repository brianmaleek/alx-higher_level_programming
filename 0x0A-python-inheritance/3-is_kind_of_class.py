#!/usr/bin/python3
"""
contains method is_kind_of_class
returns True if the object is an instance of, or
if the object is an instance of a class that
inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    use isinstance() to check if obj is an instance of a class
    returns True if the object is an instance of, or
    if the object is an instance of a class that
    inherited from, the specified class
    """
    return isinstance(obj, a_class)
