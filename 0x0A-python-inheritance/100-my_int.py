#!/usr/bin/python3
""" MyInt rebel class """


class MyInt(int):
    """ the my int class"""

    def __eq__(self, obj):
        """ the equality operator """
        return super().__ne__(obj)

    def __ne__(self, obj):
        """ the not equals operator """
        return super().__eq__(obj)
