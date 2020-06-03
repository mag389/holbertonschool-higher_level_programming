#!/usr/bin/python3
""" the square class file"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class from rectangle"""

    def __init__(self, size):
        """ instantiator for square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ sstring method """
        return "[Square] {}/{}".format(self.__size, self.__size)
