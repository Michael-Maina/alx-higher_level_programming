#!/usr/bin/python3
""" From Python Object to JSON String Module """


import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string) """
    return json.dumps(my_obj)
