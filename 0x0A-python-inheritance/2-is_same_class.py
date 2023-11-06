#!/usr/bin/python3
"""
module that reveals true or false if object is exactly an instance
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is exactly an instance of
        the class, False otherwise.
    """
    return type(obj) is a_class
