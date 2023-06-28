#!/usr/bin/python3

"""
Module 102-square
Defines class square with private size and public area
can access and update size
"""


class Square:
    """
    class Square definition

    Args:
        size (int): private

    Functions:
        __init__(self, size=0, position=(0, 0))
        size(self)
        size(self, value)
        area(self)
        my_print(self)
    """

    def __init__(self, size=0):
        """
        initialize Square object

        Attributes:
            size (int): default 0 if no size is passed
        """
        self.size = size

    @property
    def size(self):
        """
        size getter

        Returns:
            size (int): private
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter

        Args:
            value (int): private

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns area of square

        Returns:
            area (int): size squared
        """
        return (self.__size ** 2)

    def __eq__(self, other):
        """
        equality comparison

        Args:
            other (object): object to compare

        Returns:
            True if equal, False otherwise
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        inequality comparison

        Args:
            other (object): object to compare

        Returns:
            True if not equal, False otherwise
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        less than comparison

        Args:
            other (object): object to compare

        Returns:
            True if less, False otherwise
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        less than or equal to comparison

        Args:
            other (object): object to compare

        Returns:
            True if less or equal, False otherwise
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        greater than comparison

        Args:
            other (object): object to compare

        Returns:
            True if greater, False otherwise
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        greater than or equal to comparison

        Args:
            other (object): object to compare

        Returns:
            True if greater or equal, False otherwise
        """
        return (self.area() >= other.area())
