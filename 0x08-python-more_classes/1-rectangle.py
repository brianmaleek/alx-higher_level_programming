#!/usr/bin/python3


class Rectangle:
    """
    Defines class rectangle with private instance attributes.

    Functions:
        __init__(self, width, height).
        width(self, value).
        height(self, value).
        width(self).
        height(self).
    Args:
        width (int): integer width of rectangle.
        height (int): integer height of rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize data."""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
