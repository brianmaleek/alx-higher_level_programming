#!/usr/bin/python3

"""
Module for my_list
Contains a class MyList that inherits from list
"""


class MyList(list):
    """Class MyList inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
