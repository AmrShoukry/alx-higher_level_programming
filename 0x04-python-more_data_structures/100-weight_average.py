#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    score = 0
    for one_tuple in my_list:
        a, b = one_tuple
        a = a * b
        score += a
        weight += b
    return score/weight
