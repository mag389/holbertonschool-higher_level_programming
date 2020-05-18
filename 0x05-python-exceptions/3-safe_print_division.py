#!/usr/bin/python3
def safe_print_division(a, b):
    j = 0
    try:
        j = a / b
    except:
        j = None
    finally:
        print("Inside result: {}".format(j))
        return j
