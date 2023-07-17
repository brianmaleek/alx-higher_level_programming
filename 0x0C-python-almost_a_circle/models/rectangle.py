#!/usr/bin/python3

"""
Module contains class Rectangle
inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    define Class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize instance of Rectangle
        Constructor method
        Attributes:
            width: private instance attribute
            height: private instance attribute
            x: private instance attribute
            y: private instance attribute
            id: public instance attribute
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y
