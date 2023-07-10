#!/usr/bin/python3
"""
contains class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    Methods:
        __init__(self, width, height)
        area(self)
        __str__(self)
    """
    def __init__(self, width, height):
        """
        initializes a Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns the string representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
