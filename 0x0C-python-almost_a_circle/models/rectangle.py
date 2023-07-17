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

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        self.validate_value("width", value, False)
        self.__width = value

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        self.validate_value("height", value, False)
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        self.validate_value("y", value)
        self.__y = value

    def validate_value(self, name, value, eq=True):
        """
        validate value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """
        returns area of rectangle
        """
        return self.width * self.height
