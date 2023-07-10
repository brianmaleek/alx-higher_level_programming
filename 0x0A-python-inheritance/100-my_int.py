#!/usr/bin/python3
"""
contains class MyInt
"""


class MyInt(int):
    """
    Represents a MyInt
    Method:
        __init__(self, num)
        __eq__(self, other)
        __ne__(self, other)
    """
    def __init__(self, num):
        """
        initializes a MyInt
        Args:
            num (int): number
        """
        self.num = num

    def __eq__(self, other):
        """
        Returns:
            True if the numbers are not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Returns:
            True if the numbers are equal
        """
        return self.num == other
