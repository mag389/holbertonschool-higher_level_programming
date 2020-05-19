#!/usr/bin/python3
"""slightly different square class"""


class Square:
    """
    Square - the square class

    Currently blank class
    __init__ - makes instance
    """
    def __init__(self, size=0):
        """
        creates square instance

        _Square_size: self explanatory
        """
        self.__size = size

    def area(self):

        """returns square area"""

        return self.__size ** 2

    @property
    def size(self):

        """getter for size"""

        return self.__size

    @size.setter
    def size(self, value):

        """sets the size attribute"""

        if type(value) is not int:
            raise(TypeError("size must be an integer"))
        if value < 0:
            raise(ValueError("size must be >= 0"))
        self.__size = value

    def __lt__(self, other):
        """ less than"""
        return self.__size < other.__size

    def __le__(self, other):
        """ less than or equal"""
        return self.__size <= other.__size

    def __eq__(self, other):
        """ test equality"""
        return self.__size == other.__size

    def __ne__(self, other):
        """ not equal"""
        return self.__size != other.__size

    def __gt__(self, other):
        """ greater than"""
        return self.__size > other.__size

    def __ge__(self, other):
        """ greater than or equal"""
        return self.__size >= other.__size
