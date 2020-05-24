#!/usr/bin/python3
""" as of now empty rectangle class """


class Rectangle:
    """ the rectangle class """
    def __init__(self, width=0, height=0):
        """ instantiation for rectangle"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """width getter"""
        return self.__width

    @height.setter
    def height(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value