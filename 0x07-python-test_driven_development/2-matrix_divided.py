#!/usr/bin/python3
"""seond (#1) assignment"""


def matrix_divided(matrix, div):
    """ divided all elements of a matrix"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for line in matrix:
        if not isinstance(line, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for line in matrix:
        for num in line:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    line_len = len(matrix[0])
    for line in matrix:
        if len(line) is not line_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [[round(j / div, 2) for j in line] for line in matrix]
    return newmatrix
