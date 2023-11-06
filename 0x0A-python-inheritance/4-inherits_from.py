#!/usr/bin/python3
"""
module for inherits_from function
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.

    Args:
        obj (object): The object to check.
        a_class (type): The class to compare with.

    Returns:
        bool: True if the object is an instance of a class that inherited
        from the class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
