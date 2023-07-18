#!/usr/bin/python3
"""
Module contains class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    define Class Square
    inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes instance of Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        returns string representation of Square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for size - sets width and height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
