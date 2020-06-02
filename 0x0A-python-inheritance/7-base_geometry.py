#!/usr/bin/python3
""" base geo class with area"""


class BaseGeometry:
    """ the base geometry class"""

    def area(self):
        """ area method, not done because this is base geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
