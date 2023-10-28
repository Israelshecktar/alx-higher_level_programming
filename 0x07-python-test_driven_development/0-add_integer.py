#!/usr/bin/python3
"""
This module enatils a function add_integer that adds two integers together.
"""


def add_integer(a, b=98):
    """
    function Adds two integers together.
    If a or b are not integers or floats, a TypeError is raised.
    If a or b are floats, they are casted to integers.
    Returns the sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
