#!/usr/bin/python3
for character in range(97, 123):
    if character == 101:
        continue
    elif character == 113:
        continue
    print("{:c}".format(character), end='')
