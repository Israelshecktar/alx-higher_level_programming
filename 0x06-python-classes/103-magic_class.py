#!/usr/bin/python3
"""Class that performs operations on a radius"""


import math


class MagicClass:
    """
    Represents a class that performs operations on a radius.

    Attributes:
        __radius (float): The radius value.
    """

    def __init__(self, radius):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (int or float): The radius value.

        Raises:
            TypeError: If the radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates the area of a circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates the circumference of a circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
