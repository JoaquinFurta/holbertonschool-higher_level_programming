#!/usr/bin/python3
""" rectangle class """


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherince from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a new rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """sets width value"""
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """sets height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """sets x value"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """sets y value"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """displays rectangle"""
        print("".join("\n" for idx in range(self.__y)), end="")
        strr = "".join(" " for idx in range(self.__x)) + "#" * self.__width
        print("".join(strr + '\n' if idx != self.__height - 1
                      else strr for idx in range(self.__height)))

    def __str__(self):
        """prints attributes of the rectangle"""
        return "{} ({}) {}/{} - {}/{}".format(
                "[Rectangle]", self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the rectangle"""

        if args:
            try:
                super().__init__(args[0])
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """print a dictionarty of the attributes of the class"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
