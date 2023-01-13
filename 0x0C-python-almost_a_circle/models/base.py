#!/usr/bin/python3
""" Base Class Module """


class Base:
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the id attribute of an instance of the class """
        self.id = id

    @property
    def id(self):
        """ Returns id of instance """
        return self.__id

    @id.setter
    def id(self, id):
        """ Sets id """
        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects
