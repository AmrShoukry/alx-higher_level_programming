#!/usr/bin/python3
""" 3. Error code #0 """
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            html = response.read()
            decoded_page = html.decode('utf-8')
            print(decoded_page)
    except urllib.error.HTTPError as Error:
        print(f"Error code: {Error.code}")
