#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 1:
        c = 32
    else:
        c = 0
    print("{}".format(chr(122 - i - c)), end='')
