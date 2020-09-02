#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastd = -number % 10
    lastd = -lastd
if number > 0:
    lastd = number % 10

print("Last digit of {} is {} ".format(number, lastd), end='')

if lastd == 0:
    print("and is 0")
elif lastd < 6:
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
