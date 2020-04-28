#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            c = 32
        else:
            c = 0
        print("{}".format(chr(ord(i) - c)), end='')
    print()
