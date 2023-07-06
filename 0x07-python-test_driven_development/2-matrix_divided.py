#!/usr/bin/python3
"""
module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function:
        that divides all elements of a matrix

    Args:
        matrix (list of lists of ints/floats): matrix to divide
        div (int/float): divisor

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats
        TypeError: if matrix contains rows of different sizes
        TypeError: if div is not an int/float
        ZeroDivisionError: if div is 0

    Returns:
        list of lists of ints/floats: matrix divided by div
    """
    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    div_error = "div must be a number"

    if type(div) not in [int, float]:
        raise TypeError(div_error)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(matrix_error)

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
