#!/usr/bin/python3
if __name__ == "__main__":
    from sys import *
    print("{:d} argument".format(len(argv) - 1), end='')
    if len(argv) is 1:
        print("s.")
    elif len(argv) is 2:
        print(":")
        print("{:d}: {}".format(1, argv[1]))
    else:
        print("s:")
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
