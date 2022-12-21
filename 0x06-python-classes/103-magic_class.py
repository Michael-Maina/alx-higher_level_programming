#!/usr/bin/python3
""" Magic Class Module """
import math


class MagicClass:
    """ Magic class """
    def __init__(self, radius=0):
        """ Initializates the instance """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ calculate the area of a instance """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Calculates the circumference of a instance """
        return 2 * math.pi * self.__radius
