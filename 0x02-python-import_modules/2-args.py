#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    else:
        if length == 1:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(length))
        for i in range(length + 1):
            if i == 0:
                continue
            print("{:d}: {}".format(i, sys.argv[i]))
