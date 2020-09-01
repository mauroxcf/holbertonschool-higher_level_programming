#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) in range(97, 123):
            a = ord(a) - 32
            print("{:c}".format(a), end='')
        else:
            print("{:s}".format(a), end='')

