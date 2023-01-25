#!/usr/bin/python3
"""
Text identation module
contains:
text_indentation function
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    beginning = True
    for i in text:
        if beginning and i == " ":
            continue
        if beginning and i != " ":
            beginning = False
        if beginning is False:
            if i == "." or i == "?" or i == ":":
                print("{}\n".format(i))
                beginning = True
            else:
                print(i, end="")
