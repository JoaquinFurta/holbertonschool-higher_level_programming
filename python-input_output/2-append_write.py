#!/usr/bin/python3
""" function that appends string at the end of a text file
    returns number of characters added"""


def append_write(filename="", text=""):
    """ it recives filename and text to append"""

    with open(filename, "a", encoding="utf-8") as f:
        w = f.write(text)
        return w
