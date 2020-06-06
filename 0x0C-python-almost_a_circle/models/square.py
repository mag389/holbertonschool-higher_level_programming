#!/usr/bin/python3
""" the square class file """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ the square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation method for squares"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the official string represenatation """
        retstr = "[Square] ({}) {}/{} - ".format(self.id, self.x, self.y)
        retstr += str(self.width)
        return retstr

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, size):
        """ size setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update the squares values """
        if args is not None and len(args) is not 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ to dict method """
        newdict = super().to_dictionary()
        newdict["size"] = newdict["width"]
        newdict.pop("width")
        newdict.pop("height")
        return newdict
