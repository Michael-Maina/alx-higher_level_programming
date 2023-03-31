#!/usr/bin/python3
"""
script to list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
from sys import argv
import requests


if __name__ == "__main__":
    usr = argv[2]
    repo = argv[1]
    url = "https://api.github.com/repos/" + usr + "/" + repo + "/commits"
    headers = {"Accept": "application/vnd.github+json"}
    parameters = {"author": usr, "per-page": 10}

    r = requests.get(url, headers=headers, params=parameters)
    result = r.json()

    for i in range(10):
        sha = result[i].get("sha")
        author_name = result[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
