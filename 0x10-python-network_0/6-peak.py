#!/usr/bin/python3
"""
Function to find a number in a list, whos its highter that the next one,
 this numbers its call it peak and it can be more than one in the list
"""


def find_peak(list_of_integers):
    """
    find the peak of a list of integers
    """
    temp = None
    length = len(list_of_integers)
    for i in range(len(list_of_integers)):

        if list_of_integers[i] > 0:
            temp = list_of_integers[i]

        if i < length - 1:

            if temp is None or temp < list_of_integers[i+1]:
                continue

            if temp > list_of_integers[i+1]:
                    return temp

        else:
            return temp
