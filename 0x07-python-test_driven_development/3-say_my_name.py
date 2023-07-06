#!/usr/bin/python3
"""
module that prints My name is <first name> <last name>
takes 2 arguments: first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function:
        prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string

    Returns:
        None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
