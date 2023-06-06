#!/usr/bin/python3
"""
Task2
TDD
    def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Function to divide matrix byt a number
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(message)
    counter = -1
    for List in matrix:
        if not isinstance(List, list):
            raise TypeError(message)
        if counter == -1:
            counter = len(List)
        if len(List) != counter:
            raise TypeError("Each row of the matrix must have the same size")

        for item in List:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(message)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)

    return new_matrix
