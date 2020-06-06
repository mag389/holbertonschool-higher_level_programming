#!/usr/bin/python3
""" the unit tests for assignment 0 """


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ the unit testing class for base """

    def test_baseinit(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
