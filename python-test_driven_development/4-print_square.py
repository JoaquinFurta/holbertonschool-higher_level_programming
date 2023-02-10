#!/usr/bin/python3

""" function that prints a square with the character #"""


def print_square(size):

    """ prints squeare of size: size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    strn = "".join("#" for idx in range(size))
    if (size > 0):
        print("".join(strn + "\n" if idx != size - 1
                      else strn for idx in range(size)))
