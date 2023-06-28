#!/usr/bin/python3

"""Square Class"""


class Square:
    """define Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        intitalizes square
        private attribute size thats optional
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method: position of square"""
        size_str = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            self.__position = None
            raise TypeError(size_str)
        elif len(value) != 2:
            self.__position = None
            raise TypeError(size_str)
        elif type(value[0]) is not int or type(value[1]) is not int:
            self.__position = None
            raise TypeError(size_str)
        elif value[0] < 0 or value[1] < 0:
            self.__position = None
            raise TypeError(size_str)
        else:
            self.__position = value

    def area(self):
        return (self.__size) ** 2

    def my_print(self):
        """prints square to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.__size))
