#!/usr/bin/python3
""" takes in website, returns header """
from urllib import request
import sys


if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as response:
        content = response.info()
    print(content.get("X-Request-Id"))
