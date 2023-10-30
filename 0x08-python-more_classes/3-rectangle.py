#!/usr/bin/python3
"""
This module represent a pyhton object class of a rectangle
"""


class Rectangle:
    """
        This class class Rectangle that defines a rectangle by:
            (based on 2-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """initializes the width and height"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.height = height

    @property
    def width(self):
        """define the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width and assign values to it"""
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
        """assign value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """get the area"""
        return self.width * self.height

    def perimeter(self):
        """get the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """get the official representation of the width in str format"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        """return the value of area and perimeter in str format"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
