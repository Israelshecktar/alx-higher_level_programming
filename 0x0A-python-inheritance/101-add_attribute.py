#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        obj (object): The object to modify.
        name (str): The name of the attribute to add.
        value (any): The value of the attribute to add.

    Raises:
        TypeError: If the object can't have new attribute.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
