#!/usr/bin/env python3
def no_c(my_string):
    characters = []
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        characters.append(i)
    new_string = "".join(characters)
    return new_string
