#!/usr/bin/python3
""" Student Class Module """


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initializes the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Function returns the dictionary
        description of a Student instance """
        return self.__dict__
