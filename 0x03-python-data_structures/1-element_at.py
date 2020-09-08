#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx > len(my_list):
            print("none")
        elif idx < 0:
            print("none")
        else:
            return my_list[idx]
