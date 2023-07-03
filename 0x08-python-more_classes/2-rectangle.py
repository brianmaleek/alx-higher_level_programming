#!/usr/bin/python3
""" Module for Rectangle class. """


class Rectangle:
    """
    Define class Rectangle with private attribute and height.

    Args:
        width (int): width of the Rectangle
        height (int): height of the Rectangle

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """

    def __init__(self, width=0, height=0):
        """ initialization """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width: returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width: sets width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height: returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height: sets height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area: returns the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter: returns the perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
