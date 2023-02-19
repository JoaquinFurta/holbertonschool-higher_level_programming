#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes Base  class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return str(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(Base.to_json_string([obj.to_dictionary()
                                        for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """  returns the list of the JSON string representation"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary is not None:
            if cls.__name__ == "Rectangle":
                inst = cls(1, 1)
            else:
                inst = cls(1)
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", encoding='utf-8') as f:
                inst = Base.from_json_string(f.read())
            return [cls.create(**elem) for elem in inst]
        except FileNotFoundError:
            return []
