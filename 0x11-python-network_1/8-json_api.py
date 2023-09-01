#!/usr/bin/python3
""" 8. Search API """
import requests
import sys

if __name__ == '__main__':
    q = ""
    if len(sys.argv) != 1:
        q = sys.argv[1]

    data = {'q': q}

    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=data)

    try:
        json_response = response.json()

        if len(json_response) == 0:
            print("No result")
        else:
            print(f"[{json_response['id']}] {json_response['name']}")

    except requests.exceptions.RequestException:
        print("Not a valid JSON")
