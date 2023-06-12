#!/usr/bin/python3
""" Module """


class MyInt(int):
    """ Class """

    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return self.__value != other

    def __ne__(self, other):
        return self.__value == other
