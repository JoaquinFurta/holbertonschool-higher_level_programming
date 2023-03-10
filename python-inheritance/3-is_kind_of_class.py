#!/usr/bin/python3
"""returns True if the object is an instance of, or if
    the object is an instance of a class
    that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """
    args:
        obj: an object
        a_class: a class
    """
    return isinstance(obj, a_class)
