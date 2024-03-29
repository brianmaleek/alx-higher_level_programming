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

    def display(self):
        """
        prints rectangle with #
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        returns string representation of rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns dictionary representation of Rectangle
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
