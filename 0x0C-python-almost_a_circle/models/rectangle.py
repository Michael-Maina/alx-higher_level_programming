#!/usr/bin/python3
""" Rectangle Class Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class, Subclass of Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a rectangle with size attributes """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width of rectangle """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of rectangle """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x """
        if not type(value) == int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y """
        if not type(value) == int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle to stdout using # """
        for i in range(self.__height):
                print("#" * self.__width)

    def __str__(self):
        """ Returns a string representation of the Rectangle class """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
    "".format(self.id, self.__x, self.__y, self.__width, self.__height)
