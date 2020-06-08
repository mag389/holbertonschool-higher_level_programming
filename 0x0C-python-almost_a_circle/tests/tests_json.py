#!/usr/bin/python3
""" the testing for the json functions worked better as it's own file"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import json


class testJson(unittest.TestCase):
    """ class for testing json conversion """

    def test_json(self):
        """ testing for the various json conversions """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        r1dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        self.assertEqual(r1dict, dictionary)
        json_dict = Base.to_json_string([dictionary])
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            readlines = f.read()
        r3 = Rectangle.create(**r1dict)
        self.assertEqual(str(r3), "[Rectangle] (1) 2/8 - 10/7")
        list_input = [r1, r2, r3]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertEqual(r1 == list_output[1], False)
        self.assertEqual(str(r1),  "[Rectangle] (1) 2/8 - 10/7")
