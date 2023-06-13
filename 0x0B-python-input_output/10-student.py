#!/usr/bin/python3
""" Model """


class Student:
    """ Class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        length = 0
        if type(attrs) is list:
            for attribute in attrs:
                if attribute in self.__dict__ and type(attribute) is str:
                    length = 1
            if length == 0:
                return self.__dict__
            return {a: getattr(self, a) for a in attrs if a in self.__dict__}
        return self.__dict__
