#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
        print(my_list)
        return my_list[-1]
