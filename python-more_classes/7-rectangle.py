#!/usr/bin/python3
"""Creates a empty class called Rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        strn = "".join([str(self.print_symbol) for idx in range(self.__width)])
        return ("".join(strn + "\n" if idx != self.__height - 1
                else "".join(strn) for idx in range(self.__height)))

    def __repr__(self):
        rp = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return rp

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
