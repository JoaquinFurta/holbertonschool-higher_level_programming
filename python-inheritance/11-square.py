#!/usr/bin/python3
""" A subclass of rectangle called Square """


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square  """

    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
