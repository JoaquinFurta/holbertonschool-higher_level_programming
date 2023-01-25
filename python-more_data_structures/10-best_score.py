#!/usr/bin/python3
def best_score(a_dictionary):
    maxx = 0
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if value > maxx:
            maxx = value
            person = key
    return person
