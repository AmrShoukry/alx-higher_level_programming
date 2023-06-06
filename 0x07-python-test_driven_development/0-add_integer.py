#!/usr/bin/python3
"""
Task0
TDD
    def add_integer(a, b=98):
"""


def add_integer(a, b=98):
    """
    function to add integers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
