#!/usr/bin/python3
def magic_string(string=[]):
    string.append('Holberton')
    return str(string).strip('[i\']').replace('\'', '')
