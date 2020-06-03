#!/usr/bin/python3
""" script to add arguments to a python list then add to file """
import sys
import json
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    listy = load_from_json_file("add_item.json")
except:
    listy = []

for i in range(1, len(sys.argv)):
    listy.append(sys.argv[i])

save_to_json_file(listy, "add_item.json")
