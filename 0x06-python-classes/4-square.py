#!/usr/bin/pyhton3
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
