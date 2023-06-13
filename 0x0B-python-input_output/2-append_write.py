#!/usr/bin/python3
""" Model """


def append_write(filename="", text=""):
    """ Function """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
