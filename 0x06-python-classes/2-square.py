#!/usr/bin/python3

"""Square Class with private instance attribute"""


class Square:
    """Square Class with private instance attribute"""

    def __init__(self, size=0):
        """__init__ method intiailizes a size for the square
        Attributes:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
