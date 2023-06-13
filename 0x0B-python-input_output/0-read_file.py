#!/usr/bin/python3
""" Model """


def read_file(filename=""):
    """ Function """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
