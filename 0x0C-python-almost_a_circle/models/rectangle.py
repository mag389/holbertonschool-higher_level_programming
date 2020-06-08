#!/usr/bin/python3
""" Rectangle class file """
from models.base import Base


class Rectangle(Base):
    """ the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation for rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns rectangles area """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle to stdout """
        for i in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            print(" " * self.__x, end="")
            for j in range(0, self.width):
                print("#", end="")
            print("")

    def __str__(self):
        retstr = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        retstr += " - {}/{}".format(self.__width, self.__height)
        return retstr

    def update(self, *args, **kwargs):
        """ update the rectangle with an ordered args list """
        if args is not None and len(args) is not 0:
            length = len(args)
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length >= 5:
                self.y = args[4]
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """return the dict representation of the rectangle """
        newdict = {}
        newdict['id'] = self.id
        newdict['width'] = self.__width
        newdict['height'] = self.__height
        newdict['x'] = self.__x
        newdict['y'] = self.__y
        return newdict
