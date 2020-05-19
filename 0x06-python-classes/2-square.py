#!/usr/bin/python3
"""square with attribute file"""


class Square:
    """
    Square - the square class

    Currently blank class
    __init__ - makes instance
    """

    def __init__(self, _Square_size=0):
        """
        creates square instance

        _Square_size: self explanatory
        """
        if type(_Square_size) is not int:
            raise(TypeError("size must be an integer"))
        if _Square_size < 0:
            raise(ValueError("size must be >= 0"))
        self._Square__size = _Square_size
