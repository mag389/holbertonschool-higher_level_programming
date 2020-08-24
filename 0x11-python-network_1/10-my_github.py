#!/usr/bin/python3
""" showing my github id """
import requests
import sys


if __name__ == '__main__':
    uname = sys.argv[1]
    url = "https://api.github.com/users/{}".format(uname)
    token = sys.argv[2]
    # data = {"username": uname, "password": token}
    # autho = (uname, token)
    headers = {'authorization': 'token ' + token}
    try:
        r = requests.get(url, headers=headers)
        print(r.json().get("id"))
    except:
        print("Error somewhere")
