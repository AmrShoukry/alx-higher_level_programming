#!/usr/bin/python3
""" 10. Time for an interview! """
import requests
import sys

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)
    json_response = response.json()

    for i in range(10):
        print(f"{json_response[i].get('sha')}\
 {json_response[i].get('commit').get('author').get('name')}")
