#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= len(my_list):
        return None
    if idx < 0:
        return None
    else:
        for i in range(len(my_list)):
            if i == idx:
                my_list.insert(idx, element)
                return my_list
