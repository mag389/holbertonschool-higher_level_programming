#!/usr/bin/python3
def print_last_digit(number):
    c = number % 10
    if number < 0:
        c = -1 * (c - 10)
    print(c, end='')
    return c
