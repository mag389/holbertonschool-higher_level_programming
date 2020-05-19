#!/usr/bin/python3
""" magic class bytecode"""
import math


class MagicClass:
    """ the magic class"""

    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ returns circle area"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """ returns circumference"""
        return math.pi * 2 * self.__radius
