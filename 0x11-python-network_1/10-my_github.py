#!/usr/bin/python3
""" 9. My GitHub! """
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    url = f'https://api.github.com/users/{username}'

    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        response_json = response.json()
        print(response_json.get('id'))
    else:
        print("None")
