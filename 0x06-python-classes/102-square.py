#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class """

    def __init__(self, size=0):
        """ Initializes the data """
        self.size = size

    @property
    def size(self):
        """ Returns the size of a square instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of a Square instance """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculates de square's area """
        return self.__size ** 2

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())
