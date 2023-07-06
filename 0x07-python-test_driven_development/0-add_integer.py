#!/usr/bin/python3
"""
Module 0-add_integer
Contains function that adds 2 integers
Accepts int, float; otherwise raise TypeError
"""


def add_integer(a, b=98):
    """
    Function that adds 2 integers

    Typechecks: int, float; otherwise raise TypeError

    Args:
        a (int, float): first number
        b (int, float): second number

    Returns:
        int: sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
