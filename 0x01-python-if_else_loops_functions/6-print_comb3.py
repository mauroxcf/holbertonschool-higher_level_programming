#!/usr/bin/python3

for num in range(0, 10):
    for num2 in range(0, 10):
        if num2 == num:
            continue
        if num == 8 and num2 == 9:
            print("{:d}{:d}".format(num, num2))
        if num2 > num:
            print("{:d}{:d}, ".format(num, num2), end="")
