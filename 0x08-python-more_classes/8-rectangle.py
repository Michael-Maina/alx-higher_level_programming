#!/usr/bin/python3
""" Rectangle Module """


class Rectangle:
    """ Rectangle Class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter function for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finds area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Finds perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints text on deletion of an instance of the rectangle class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
