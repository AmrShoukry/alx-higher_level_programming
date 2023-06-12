#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """ Method """

    return isinstance(obj, a_class) and type(obj) != a_class
