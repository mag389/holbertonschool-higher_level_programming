#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    j = 0
    for i in str:
        if j != n:
            s += i
        j = j + 1
    return s
