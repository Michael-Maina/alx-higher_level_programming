#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class """

    def __init__(self, size=0):
        """ Initializes the data """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculates de square's area """
        return self.__size ** 2
