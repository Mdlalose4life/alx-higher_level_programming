#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arguments = len(argv)
    i = 1
    if arguments == 0:
        print("{:d} arguments.".format(arguments))
    elif arguments == 1:
        print("{:d} arguments.".format(arguments))
        print("{:d}: {:s}".format(i, argv))
    else:
        print("{:d} arguments.".format(arguments))
        while i <= arguments:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
