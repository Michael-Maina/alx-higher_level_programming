#!/usr/bin/python3
""" Append file Module """


def append_write(filename="", text=""):
    """ Function writes a string to a text file(UTF-8)
    returns the number of characters written """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
