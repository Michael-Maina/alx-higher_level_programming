#!/usr/bin/python3
""" Read File Module """


def read_file(filename=""):
    """ Function reads a text file(UTF-8) and prints it to stdout """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        print(my_file.read(), end='')
