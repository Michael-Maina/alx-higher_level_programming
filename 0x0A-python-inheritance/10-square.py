#!/usr/bin/python3
""" Contains the BaseGeometry Class and Rectangle Sub Class """


class BaseGeometry:
    """ BaseGeometry Class """

    def area(self):
        """ Raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle Sub Class of BaseGeometry """

    def __init__(self, width, height):
        """ Initializes data for the rectangle class """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """ Returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Defines print output """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Square Sub Class of Rectangle """

    def __init__(self, size):
        """ Initializes data for the square class """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns the area of a square """
        return self.__size * self.__size
