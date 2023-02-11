#!/usr/bin/python3

""" add newlines to a text when it contains (., ?, :)"""


def text_indentation(text):
    """ add newlines to a text when it contains (., ?, :)"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print("".join([elem if elem not in ".?:" else elem + "\n\n"
                   for elem in text])
            .replace("\n ", "\n").replace("\n  ", "\n"), end="")
