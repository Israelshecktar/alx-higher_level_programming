#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_valid_lists(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, "2", 3, 4])
        self.assertEqual(max_integer([10**18, 10**19, 10**20]), 10**20)
        self.assertEqual(max_integer([11]), 11)
        self.assertEqual(max_integer([11]), 11)
        self.assertEqual(max_integer("a"), "a")
        self.assertEqual(max_integer(["a"]), "a")
        self.assertEqual(max_integer(["a", "b", "A", "Z", "z"]), "z")

    def test_invalid_lists(self):

        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, [1, "5", 3, "9", 2])
        self.assertRaises(TypeError, max_integer, [1, 2], [], [3, 4])
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
