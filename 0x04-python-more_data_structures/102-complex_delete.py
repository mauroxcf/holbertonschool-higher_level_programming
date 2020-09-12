#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value:
        new_dictionary = a_dictionary.copy()
        for i, j in new_dictionary.items():
            if value == j:
                del a_dictionary[i]
        return a_dictionary
