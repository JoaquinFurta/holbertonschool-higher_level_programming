#!/usr/bin/python3
""" A function that prints names """


def say_my_name(first_name, last_name=""):
    """ print name in standar output"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
