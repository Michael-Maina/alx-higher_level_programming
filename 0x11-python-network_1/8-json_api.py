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
        if req.status_code == 204 or req.json() == {}:
            print("No result")
        else:
            result = req.json()
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
