#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return (None)
    dict2 = {}
    for x, y in a_dictionary.items():
        dict2[x] = y * 2
    return (dict2)
