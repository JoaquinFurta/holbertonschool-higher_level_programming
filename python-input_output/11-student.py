#!/usr/bin/python3
""" Class Stuedent with to_json and reload_from_json methods"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            return {val: self.__dict__[val] for val in attrs
                    if val in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in self.__dict__:
            if key in json:
                self.__dict__[key] = json[key]
