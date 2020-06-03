#!/usr/bin/python3
""" insert new line of text between lines """


def append_after(filename="", search_string="", new_string=""):
    """ searches for search string in file
        if found adds new string as next line
    """
    with open(filename, 'r') as f:
        filetext = f.readlines()
    for line in range(0, len(filetext)):
        if search_string in filetext[line]:
            filetext.insert(line + 1, new_string)
    with open(filename, 'w') as f:
        f.write("".join(filetext))
