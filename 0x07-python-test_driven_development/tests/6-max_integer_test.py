#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ the unit testing class"""

    def test_allnums(self):
        """test with all numbers"""
        max_integer([1, 2, 3, 4]) == 4
        max_integer([1, 3, 4, 2]) == 4

    def test_values(self):
        """checking for bad values"""
        self.assertRaises(TypeError, max_integer, 7)
