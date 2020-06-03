#!/usr/bin/python3
""" insert new line of text between lines """


def append_after(filename="", search_string="", new_string=""):
    """ searches for search string in file
        if found adds new string as next line
    """
    with open(filename, 'r') as f:
        filetext = f.readlines()
    insertindex = 1
    textcpy = list(filetext)
    for line in range(0, len(textcpy)):
        if search_string in textcpy[line]:
            filetext.insert(insertindex, new_string)
            insertindex += 1
        insertindex += 1
    with open(filename, 'w') as f:
        f.write("".join(filetext))
