#!/usr/bin/python3
""" sends post request containing an e-mail"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    email = sys.argv[2]
    url = sys.argv[1]
    data = parse.urlencode({'email': email})
    data = data.encode('ascii')
    # req = request.Request(url, data)
    with request.urlopen(url, data) as response:
        content = response.read()
    print(content.decode('utf-8'))
