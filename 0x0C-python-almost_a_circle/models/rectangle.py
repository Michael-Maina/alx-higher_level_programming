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
        self.__width = value

    @property
    def height(self):
        """ Returns height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of rectangle """
        self.__height = value

    @property
    def x(self):
        """ Returns x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x """
        self.__x = value

    @property
    def y(self):
        """ Returns y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y """
        self.__y = value
