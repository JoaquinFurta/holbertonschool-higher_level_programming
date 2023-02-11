#!/usr/bin/python3
""" A subclass from Rectangle called Square """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Squeare """

    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
