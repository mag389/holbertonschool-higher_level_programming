#!/usr/bin/python3
""" find peak"""


def find_peak(list_of_integers):
    """ finds peak in the list"""
    length = len(list_of_integers)
    l = list_of_integers
    mid = int(length / 2)
    # print(list_of_integers)
    # print("mid: {} and l:{}".format(mid, length))
    if length < 1:
        return None
    if length == 1:
        return list_of_integers[0]
    left = -100000000
    if mid > 0:
        left = list_of_integers[mid - 1]
    right = -999999999
    if mid < length - 1:
        right = list_of_integers[mid + 1]
    if l[mid] > left and l[mid] > right:
        return l[mid]
    elif l[mid] < right:
        return find_peak(l[mid + 1: length])
    elif l[mid] < left:
        return find_peak(l[0:mid])
    # else they're equal
    else:
        return max(find_peak(l[mid + 1: length]), find_peak(l[0:mid]))
