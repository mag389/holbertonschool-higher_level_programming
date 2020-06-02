#!/usr/bin/python3
""" rectangle: subclass of geometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ the rectangle class, sub of basegeometry """

    def __init__(self, width, height):
        """ instantiaition method """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
