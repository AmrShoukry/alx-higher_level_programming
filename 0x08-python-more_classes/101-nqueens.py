#!/usr/bin/python3
""" Queens Task """

import sys

arguments_length = len(sys.argv)
if (arguments_length != 2):
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def check_diagonal_availability(i, current, n, arr):
    Horizontal = i
    Vertical = current

    while (Horizontal < n and Vertical < n):
        for row in arr:
            if Vertical == row[0] and Horizontal == row[1]:
                return False
        Horizontal += 1
        Vertical += 1

    Horizontal = i
    Vertical = current

    while (Horizontal < n and Vertical >= 0):
        for row in arr:
            if Vertical == row[0] and Horizontal == row[1]:
                return False
        Horizontal += 1
        Vertical -= 1

    Horizontal = i
    Vertical = current

    while (Vertical < n and Horizontal >= 0):
        for row in arr:
            if Vertical == row[0] and Horizontal == row[1]:
                return False

        Horizontal -= 1
        Vertical += 1

    Horizontal = i
    Vertical = current

    while (Horizontal >= 0 and Vertical >= 0):
        for row in arr:
            if Vertical == row[0] and Horizontal == row[1]:
                return False

        Horizontal -= 1
        Vertical -= 1

    return True


solutions = []
arr = []

for i in range(n):
    arr.append([i, -1])

current = 0
j = 0
reserved = []

while len(reserved) < n:
    found = False
    for i in range(j, n):
        if i not in reserved:
            if check_diagonal_availability(i, current, n, arr) is True:
                arr[current][1] = i
                current += 1
                reserved.append(i)
                j = 0
                found = True
                break

    if not found:
        j = arr[current - 1][1] + 1
        arr[current - 1][1] = -1
        current -= 1
        reserved.pop()

    if len(reserved) == n:
        solutions.append([value[:] for value in arr])

        current -= 1
        j = arr[current][1] + 1
        arr[current][1] = -1
        reserved.pop()

    if arr[0][1] == n - 1:
        break

for solution in solutions:
    print(solution)
