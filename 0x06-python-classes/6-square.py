#!/usr/bin/pyhton3
class Square:
    """
    Square - the square class

    Currently blank class
    __init__ - makes instance
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        creates square instance

        _Square_size: self explanatory
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if type(value) is not tuple:
            raise(TypeError("position must be a tuple of 2 positive integers"))
        if value[1] < 0 or value[0] < 0:
            raise(TypeError("position must be a tuple of 2 positive integers"))
        self.__position = value

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

    def my_print(self):
        """ prints the square"""
        if self.__size is 0:
            print("")
        for i in range(0, self.position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.__size - 1):
                print("#", end="")
            print("#")
