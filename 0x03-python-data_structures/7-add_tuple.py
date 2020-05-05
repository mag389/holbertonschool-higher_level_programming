#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newlist = [0, 0]
    if len(tuple_a) >= 1:
        newlist[0] += tuple_a[0]
    if len(tuple_a) >= 2:
        newlist[1] += tuple_a[1]
    if len(tuple_b) >= 1:
        newlist[0] += tuple_b[0]
    if len(tuple_b) >= 2:
        newlist[1] += tuple_b[1]
    newtuple = (newlist[0], newlist[1])
    return newtuple
