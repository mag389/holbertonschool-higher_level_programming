#!/usr/bin/python3
""" sends post request containing an e-mail"""
from urllib import request, parse, error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read()
        print(content.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
