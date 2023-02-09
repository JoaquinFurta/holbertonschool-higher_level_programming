#!/usr/bin/python3

""" A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Args:
        A matrix: matrix
        The number that will divde the matrix: div
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not all(len(matrix[0]) == len(matrix[idx]) for idx in range(len(matrix))):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)"
                        + "of integers/floats")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
