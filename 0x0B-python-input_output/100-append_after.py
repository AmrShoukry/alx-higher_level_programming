#!/usr/bin/python3
""" Model """


def append_after(filename="", search_string="", new_string=""):
    """ Function """
    string = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file.readlines():
            string += line
            if search_string in line:
                string += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(string)
