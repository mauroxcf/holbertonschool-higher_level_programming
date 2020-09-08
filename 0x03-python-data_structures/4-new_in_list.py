#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    new_my_list = my_list.copy()
    if idx >= len(my_list):
        return new_my_list
    if idx < 0:
        return new_my_list
    else:
        new_my_list[idx] = new_element
        return new_my_list
