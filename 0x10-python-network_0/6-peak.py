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
    for i in range(len(list_of_integers)):

        if list_of_integers[i] > 0:
            temp = list_of_integers[i]

        if temp is None:
            continue

        if temp > list_of_integers[i+1]:
                return temp

        if temp < list_of_integers[i+1]:
            continue

        else:
            return temp

    return temp
