#!/usr/bin/python3
""" Write file Module """


def write_file(filename="", text=""):
    """ Function writes a string to a text file(UTF-8)
    returns the number of characters written """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
