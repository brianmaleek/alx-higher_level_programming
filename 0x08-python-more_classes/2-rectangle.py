#!/usr/bin/python3


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        initialize Rectangle

        Args:
            width (int): integer width
            height (int): integer height
        Funtions:
            __init__(self, width, height)
            width(self)
            width(self, value)
            height(self)
            height(self, value)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width: returns width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width: sets width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height: returns height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height: sets height"""
        if (type(value) is not int):
            raise TypeError("height must be integer")
        elif (value < 0):
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
