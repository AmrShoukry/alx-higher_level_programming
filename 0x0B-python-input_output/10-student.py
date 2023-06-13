#!/usr/bin/python3
""" Model """


class Student:
    """ Class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attributes = []
        if type(attrs) is list:
            for attribute in attrs:
                if attribute in self.__dict__:
                    attributes.append(attribute)
            if len(attributes) == 0:
                return self.__dict__     

            return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}
                        
        return self.__dict__
