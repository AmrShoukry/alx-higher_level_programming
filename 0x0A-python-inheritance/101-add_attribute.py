#!/usr/bin/python3
""" Module """


def add_attribute(obj, attribute, value):
    """ Method """

    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
