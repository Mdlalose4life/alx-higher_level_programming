#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    addition = 0
    for i in argv[1:]:
        addition += int(i)
        print("{:d}".format(addition))
