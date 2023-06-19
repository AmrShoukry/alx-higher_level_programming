#!/usr/bin/python3
""" Base Class Module """

import json
from turtle import *
import random


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            """ Serialization to a text """
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Serialization to a json file """
        file_name = f"{cls.__name__}.json"
        data = cls.to_json_string([item.to_dictionary() for item in list_objs])

        with open(file_name, "w") as file:
            file.write(data)

    @staticmethod
    def from_json_string(json_string):
        """ Deserialization from a text"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creating a new instance """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            new_instance = cls(1, 0, 0)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ Deserialization from a json file """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, "r") as file:
                data = cls.from_json_string(file.read())
        except Exception:
            return []

        instances = []
        for instance in data:
            instances.append(cls.create(**instance))

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialization to an csv file """
        file_name = f"{cls.__name__}.csv"
        data = cls.to_json_string([item.to_dictionary() for item in list_objs])

        with open(file_name, "w") as file:
            file.write(data)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialization from an csv file """
        file_name = f"{cls.__name__}.csv"

        try:
            with open(file_name, "r") as file:
                data = cls.from_json_string(file.read())
        except Exception:
            return []

        instances = []
        for instance in data:
            instances.append(cls.create(**instance))

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        myArrow = Turtle()

        # for loop
        for rectangle in list_rectangles:
            my_shape_color = Base.select_random_color()
            myArrow.setpos(rectangle.x, rectangle.y)
            myArrow.down()
            myArrow.setheading(0)
            myArrow.color(my_shape_color)
            for i in range(2):
                myArrow.forward(rectangle.width)
                myArrow.right(90)
                myArrow.forward(rectangle.height)
                myArrow.right(90)
            myArrow.penup()

        for square in list_squares:
            my_shape_color = Base.select_random_color()
            myArrow.setpos(square.x, square.y)
            myArrow.down()
            myArrow.setheading(0)
            myArrow.color(my_shape_color)
            for i in range(2):
                myArrow.forward(square.width)
                myArrow.right(90)
                myArrow.forward(square.height)
                myArrow.right(90)
            myArrow.penup()

        done()

    @staticmethod
    def select_random_color():
        colors = ["red", "green", "blue", "orange", "brown", "black", "purple"]
        return random.choice(colors)
