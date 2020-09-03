#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    acum = 0
    for i in range(1, len(argv)):
        (acum) += int(argv[i])
    print("{}".format(acum))
