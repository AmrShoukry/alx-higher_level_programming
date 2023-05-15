#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for element in row:
            if i == 0:
                print("{:d}".format(element), end="")
            else:
                print(" {:d}".format(element), end="")
            i += 1
        print("")
