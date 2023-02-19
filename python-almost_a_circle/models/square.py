""" A subclass from Rectangle called Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Squeare """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialaizes the squeare"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ print the attributes of the squeare"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """sets the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the squeare"""
        if args:
            try:
                super().__init__(self.size, self.size, self.x, self.y, args[0])
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    super().__init__(self.size, self.size, self.x, self.y, val)
                elif key == "size":
                    self.size = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """print a dictionary of the attributes of squeare"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
