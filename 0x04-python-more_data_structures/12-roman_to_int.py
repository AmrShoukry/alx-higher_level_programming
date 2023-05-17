#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    result = 0
    number = 0
    Icheck = False
    for char in roman_string:
        if char == "I":
            number = 1
            Icheck = True
        elif char == "V":
            number = 5
        elif char == "X":
            number = 10
        elif char == "L":
            number = 50
        elif char == "C":
            number = 100
        elif char == "D":
            number = 500
        elif char == "M":
            number = 1000

        result = result + number
        if char != "I":
            if Icheck is True:
                result = result - 2
            Icheck = False
    return result
