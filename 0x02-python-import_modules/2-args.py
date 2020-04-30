#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    if len(argv) is 1:
        print("0 arguments.")
    else:
        for i in range(1, len(argv)):
            print(i, " {}".format(argv[i]))
