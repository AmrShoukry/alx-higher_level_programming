#!/usr/bin/python3
"""
Task5
TDD
def text_indentation(text):
"""


def text_indentation(text):
    """
    Function to test indentation
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    mode = 1
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print("\n")
            mode = 1
        elif char == ' ':
            if mode == 1:
                continue
            else:
                print(char, end="")
        else:
            print(char, end="")
            mode = 0
