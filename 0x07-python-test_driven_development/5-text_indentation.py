#!/usr/bin/python3
"""
Module to print a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Function to print a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text (str): text to print
    Raises:
        TypeError: If text is not a string
    Returns:
        None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print("\n".join([line.strip(' ') for line in text.split("\n")]), end="")
