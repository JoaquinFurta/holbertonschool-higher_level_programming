#!/usr/bin/python3

"""Adding function"""


def add_integer(a, b=98):
    """Args to add:
            (a),(b)
       if they are not integers or floats an Error wuold be raised
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
