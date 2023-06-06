#!/usr/bin/python3
"""
Task100
TDD
def matrix_mul(m_a, m_b):
"""


def matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    counter = -1
    for List in m_a:
        if not isinstance(List, list):
            raise TypeError("m_a must be a list of lists")

        if List == []:
            raise ValueError("m_a can't be empty")

        for item in List:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("m_a should contain only integers or floats")

        if counter == -1:
            counter = len(List)
        if len(List) != counter:
            raise TypeError("each row of m_a must be of the same size")

    counter = -1
    for List in m_b:
        if not isinstance(List, list):
            raise TypeError("m_b must be a list of lists")

        if List == []:
            raise ValueError("m_b can't be empty")

        for item in List:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError("m_b should contain only integers or floats")

        if counter == -1:
            counter = len(List)
        if len(List) != counter:
            raise TypeError("each row of m_b must be of the same size")

    columns_a = len(m_a[0])
    rows_b = len(m_b)

    if columns_a == rows_b:
        m_b_transpose = list(zip(*m_b))
        new_matrix = []

        for row in m_a:
            new_row = []
            for column in m_b_transpose:
                result = 0
                for i in range(rows_b):
                    result += row[i] * column[i]
                new_row.append(result)
            new_matrix.append(new_row)
    else:
        raise ValueError("m_a and m_b can't be multiplied")
    return new_matrix
