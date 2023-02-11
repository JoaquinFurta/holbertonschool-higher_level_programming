#!/usr/bin/python3

"""returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """
        args obj: an object
        a_class : a class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
