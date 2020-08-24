#!/usr/bin/python3
""" passing a letter and testing json """
import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) > 1):
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    try:
        r = requests.post(url, data)
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            print("{} {}".format(json.get("id"), json.get("name")))
    except:
        print("Not a valid JSON")
