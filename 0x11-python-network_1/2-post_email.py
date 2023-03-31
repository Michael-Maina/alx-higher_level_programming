#!/usr/bin/python3
"""
script takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response decoded in utf-8
"""
from urllib.request import urlopen, Request
from urllib import parse
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(argv[1], header)

    with urlopen(req) as response:
        result = response.read().decode()
        print(result)