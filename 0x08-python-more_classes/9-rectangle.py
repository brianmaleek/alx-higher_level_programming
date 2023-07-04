#!/usr/bin/python3
""" Module for Rectangle class. """


class Rectangle:
    """
    Define class Rectangle with private attribute and height.

    Args:
        width (int): width of the Rectangle
        height (int): height of the Rectangle

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """__str__: prints the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        width = self.__width
        height = self.__height
        return ((str(self.print_symbol) * width + "\n") * height)[:-1]

    def __repr__(self):
        """__repr__: returns the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """__del__: deletes instance of a class"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @property
    def width(self):
        """ width: returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width: sets width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height: returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height: sets height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area: returns the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter: returns the perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal: returns the biggest rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        square: returns a new Rectangle instance with width == height == size
        """
        return (cls(size, size))
