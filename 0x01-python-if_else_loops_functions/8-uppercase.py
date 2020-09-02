#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) in range(97, 123):
            a = chr(ord(a) - 32)
        print("{}".format(a), end='')
    print("")
