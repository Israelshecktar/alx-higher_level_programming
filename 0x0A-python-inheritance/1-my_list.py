#!/usr/bin/python3
"""
module for MyList class
"""


class MyList(list):
    """A subclass of list that can print a sorted list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
