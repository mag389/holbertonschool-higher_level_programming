#!/usr/bin/python3
""" accounting for error codes """
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(requests.get(url).status_code))
