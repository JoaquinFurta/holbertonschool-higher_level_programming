#!/usr/bin/python3
""" it creates a Squeare class """


class Square:
    """
    Square class
    args: size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or\
           not all(isinstance(elem, int) for elem in value) or\
           not all(elem >= 0 for elem in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size <= 0:
            print()
        else:
            for idx in range(self.__position[1]):
                print()
            string = "".join([" " for idx in range(self.__position[0])])
            string += "".join(["#" for idx in range(self.__size)])
            for idx in range(self.__size):
                print(string)
