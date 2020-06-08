#!/usr/bin/python3
""" unittesting for the square file/class """
import unittest
from models.square import Square


class testSquare(unittest.TestCase):
    """ the square tesing class"""

    def test_init(self):
        """ tetsing basic ssquare creation
        also checks for square size getter/setter
        """
        Square._nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 12)
        s2 = Square(2, 2)
        self.assertEqual(s2.x, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (14) 1/3 - 3")
        s2.size = 5
        self.assertEqual(s2.size, 5)
        with self.assertRaises(ValueError):
            s2.size = -5

    def test_square_update(self):
        """ testing square update with"""
        s1 = Square(5, 0, 0, 11)
        self.assertEqual(str(s1), "[Square] (11) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_square_dict(self):
        """ testing for square dictionary funcitonality """
        s1 = Square(1, 1, 1, 1)
        self.assertEqual(str(s1), "[Square] (1) 1/1 - 1")
        d1 = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s1.update(**d1)
        self.assertEqual(s1.to_dictionary(), d1)
        s2 = Square(1, 1, 1, 1)
        s2.update(**d1)
        self.assertEqual(s1 == s2, False)
