#!/usr/bin/python3
"""
This module represent a pyhton object class of a rectangle
"""


class Rectangle:
    """
        This class class Rectangle that defines a rectangle by:
            (based on 1-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """define the width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """define the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """find the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height
