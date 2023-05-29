#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        type = value.__class__.__name__
        text = "Exception: Unknown format code 'd'"
        message = f"{text} for object of type '{type}'"
        print(message, file=sys.stderr)
        return False
