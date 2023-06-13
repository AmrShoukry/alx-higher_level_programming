#!/usr/bin/python3
""" Model """


def pascal_triangle(n):
    """ Method """

    if n <= 0:
        return []

    myBigList = []
    for i in range(n):
        small_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                small_list.append(1)
            else:
                small_list.append(myBigList[i-1][j-1] + myBigList[i-1][j])
        myBigList.append(small_list)
    return myBigList
