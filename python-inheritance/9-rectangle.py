#!/usr/bin/python3
"""A subclass of BaseGeometry called Rectangle """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectanlge """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def print(self):
        print(self.area())

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
