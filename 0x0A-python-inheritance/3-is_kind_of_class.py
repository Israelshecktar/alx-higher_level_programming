#!/usr/bin/python3
"""
module for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or
        if the object is an instance of a class that
        inherited from, the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the class, False otherwise.
    """
    return isinstance(obj, a_class)
