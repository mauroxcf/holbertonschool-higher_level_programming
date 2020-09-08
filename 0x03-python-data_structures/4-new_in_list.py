#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx < 0:
        return
    elif idx > len(my_list):
        return
    else:
        for i in range(len(my_list)):
            if i == idx:
                new_my_list = my_list.copy()
                new_my_list[i] = new_element
                return new_my_list
