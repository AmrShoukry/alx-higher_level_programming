#!/usr/bin/python3
for i in range(10):
    for j in range(9):
        if j > i:
            print("{:d}".format(i), end="")
            print("{:d}, ".format(j), end="")
print("89")
