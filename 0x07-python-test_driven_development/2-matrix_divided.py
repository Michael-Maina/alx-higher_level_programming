#!/usr/bin/python3
"""
Matrix divided module
contains:
matrix_divided fucntion
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 \
       or any(len(row) == 0 for row in matrix) \
       or any(type(row) is not list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    if any(len(matrix[0]) != len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(col / div, 2) for col in row] for row in matrix]
