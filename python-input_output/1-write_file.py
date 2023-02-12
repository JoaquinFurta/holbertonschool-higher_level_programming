#!/usr/bin/python3
""" writes a string to a text file and
    returns number of characters wrriten"""


def write_file(filename="", text=""):
    """ it recives a filename and text to write"""

    with open(filename, "w", encoding="utf-8") as f:
        w = f.write(text)
        return w
