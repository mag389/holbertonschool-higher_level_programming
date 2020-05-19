#!/usr/bin/python3
""" magic class bytecode"""
import math


class MagicClass:
    """ the magic class"""

    def __init__(self, radius):
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self):
        """ returns circle area"""
        return math.pi * self.radius ** 2

    def circumference(self):
        """ returns circumference"""
        return math.pi * 2 * self.radius
