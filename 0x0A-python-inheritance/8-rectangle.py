#!/usr/bin/python3
"""
contains class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a subclass Rectangle
    """
    def __init__(self, width, height):
        """
        initializes a Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
