#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception:
        print(f"{value} is not an integer")
