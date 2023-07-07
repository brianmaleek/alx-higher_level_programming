#!/usr/bin/python3
"""
    4-print_square.py
    Module that defines a function that prints a square with the character #
"""


def print_square(size):
    """
    Function:
        print_square - Prints a square with the character #
    Args:
        size (int): Size of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
