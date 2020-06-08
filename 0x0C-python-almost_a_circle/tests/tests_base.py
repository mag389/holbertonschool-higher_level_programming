#!/usr/bin/python3
""" the unit tests for assignment 0 """


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ the unit testing class for base """

    def test_baseinit(self):
        """ basic tests for number 1 """
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_first_rect(self):
        """ tests for beginning of rectangle assignment 2 """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 4)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
