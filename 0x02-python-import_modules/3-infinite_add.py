#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    if len(argv) is 1:
        print("{}".format(0))
        exit()
    r = 0
    for i in range(1, len(argv)):
        r += int(argv[i])
    print(r)
