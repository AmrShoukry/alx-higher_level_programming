#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    dictionary["M"] = 1000
    result = 0
    number = 0
    previous = 0
    for char in roman_string:
        if dictionary[char] > previous and previous != 0:
            result = result - (previous * 2)
        result = result + dictionary[char]
        previous = dictionary[char]
    return result
