#!/usr/bin/python3

"""
Module 101-square
Define class Square with private instance attribute size and position
Define myprint(self) to print to stdout the square with the character #
"""


class Square:
    """
    class Square definition

    Args:
        size (int): private
        position (tuple): private

    Functions:
        __init__(self, size=0, position=(0, 0))
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize Square object

        Attributes:
            size (int): default 0 if no size is passed
            position (tuple): tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        getter function for size

        Returns:
            size (int): private
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter function for size

        Args:
            value (int): private
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        getter function for position

        Returns:
            position (tuple): private
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter function for position

        Args:
            value (tuple): sets position to tuple of 2 positive integers
        """
        if type(value) != tuple or len(value) != 2 or \
            type(value[0]) != int or type(value[1]) != int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns area of Square object

        Returns:
            area (int): size squared
        """
        return self.size ** 2

    def my_print(self):
        """
        prints to stdout the square with the character #
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))

    def __str__(self):
        square_str = ""
        if self.size == 0:
            return square_str

        for i in range(self.position[1]):
            square_str += "\n"

        for j in range(self.size):
            square_str += " " * self.position[0] + "#" * self.size + "\n"

        return square_str.rstrip()
