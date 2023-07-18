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
