#!/usr/bin/python3
""" 2. POST an email #0 """
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        html = response.read()
        decoded_page = html.decode('utf-8')
        print(decoded_page)
