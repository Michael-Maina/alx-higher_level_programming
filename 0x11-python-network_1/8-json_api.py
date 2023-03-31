#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv[1]):
        data = {"q": ""}
    elif not isinstance(argv[1], str):
        print("No result")
    else:
        data = {"q": argv[1]}

    req = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        result = req.json()
        if len(result) == 0:
            print("No result")
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except requests.exceptions.InvalidJSONError:
        print("Not a valid JSON")
