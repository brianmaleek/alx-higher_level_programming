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
    Method:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """
        initializes a Square
        Args:
            size (int): size of the Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns the area of the Square
        """
        return self.__size ** 2

    def __str__(self):
        """
        returns the string representation of the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
