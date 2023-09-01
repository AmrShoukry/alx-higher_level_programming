#!/usr/bin/python3
""" 5. Response header value #1 """
import requests
import sys

if __name__ == '__main__':
    variable = 'X-Request-Id'
    url = sys.argv[1]

    response = requests.get(url)
    value = response.headers.get(variable)

    print(value)
