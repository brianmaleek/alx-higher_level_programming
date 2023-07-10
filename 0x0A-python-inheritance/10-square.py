#!/usr/bin/python3
"""
contains class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a Square
    inherits from Rectangle
    which inherits from BaseGeometry
    """
    def __init__(self, size):
        """
        initializes a Square
        Args:
            size (int): size of the Square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
