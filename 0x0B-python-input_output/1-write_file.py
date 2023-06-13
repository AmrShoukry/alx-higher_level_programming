#!/usr/bin/python3
""" Model """


def write_file(filename="", text=""):
    """ Function """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
