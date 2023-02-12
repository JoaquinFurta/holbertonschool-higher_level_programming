#!/usr/bin/python3
""" A function that read a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """take a filename as an argument"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
