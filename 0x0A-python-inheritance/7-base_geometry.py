#!/usr/bin/python3
"""
contains class BaseGeometry
"""


class BaseGeometry:
    """
    Represents a BaseGeometry
    """
    def area(self):
        """
        raises an exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        Args:
            name (str): name of variable
            value (int): variable to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
