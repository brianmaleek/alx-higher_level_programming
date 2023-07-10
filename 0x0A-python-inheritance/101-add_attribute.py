#!/usr/bin/python3
"""
contains method add_attribute
"""


def add_attribute(obj, name, value):
    """
    add_attribute - adds a new attribute to an object if it’s possible
    Args:
        obj - object to add attribute to
        name - name of attribute to add
        value - value of attribute to add
    Raises:
        TypeError - if obj is not able to add new attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
