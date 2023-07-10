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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
