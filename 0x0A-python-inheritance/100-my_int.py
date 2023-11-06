#!/usr/bin/python3
"""
module for MyInt class
"""


class MyInt(int):
    """A subclass of int that is a rebel"""

    def __eq__(self, other):
        """Returns the opposite of equality comparison"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns the opposite of inequality comparison"""
        return super().__eq__(other)
