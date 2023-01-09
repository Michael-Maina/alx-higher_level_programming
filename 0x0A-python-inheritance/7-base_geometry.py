#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        self.value = value
        if type(self.value) is not int:
            raise TypeError("<name> must be an integer")
        if self.value <= 0:
            raise ValueError("<name> must be greater than 0")
