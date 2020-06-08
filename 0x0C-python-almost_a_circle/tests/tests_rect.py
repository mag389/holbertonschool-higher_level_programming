#!/usr/bin/python3
""" tests for specifically the rectangle class """
import unittest
from models.rectangle import Rectangle


class testRect(unittest.TestCase):
    """ rectangle unit testing """

    def test_first_rect(self):
        """ tests for beginning of rectangle assignment 2
        additionally tests area from task 4
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 9)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 20)

    def test_rect_excepts(self):
        """ testing rectangle class for correct exceptoin #2 """
        with self.assertRaises(TypeError):
            Rectangle("hi", 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "hi", 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "hi", 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "hi", 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -9, 1)

    def test_rect_str(self):
        """ test the __str__ method"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual("[Rectangle] (12) 0/0 - 10/2", str(r3))
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1, 0, 7)
        self.assertEqual(str(r2), "[Rectangle] (7) 1/0 - 5/5")

    def test_rect_update(self):
        """ tests the rectangle update function"""
        r1 = Rectangle(10, 10, 10, 10, 12)
        self.assertEqual(r1.id, 12)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_r_update_kw(self):
        """ testing rectangle update with kwargs """
        r2 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(str(r2), "[Rectangle] (10) 10/10 - 10/10")
        r2.update(height=1)
        self.assertEqual(str(r2), "[Rectangle] (10) 10/10 - 10/1")
        r2.update(width=1, x=2)
        self.assertEqual(str(r2), "[Rectangle] (10) 2/10 - 1/1")
        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r2), "[Rectangle] (89) 3/1 - 2/1")
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r2), "[Rectangle] (89) 1/3 - 4/2")

    def test_todict(self):
        """ testing rectangle to dictionary function"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        d1 = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), d1)
        r2 = Rectangle(1, 1)
        r2.update(**d1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/9 - 10/2")
