#!/usr/bin/python3

if __name == "__main__":
    import sys
    argv = sys.argv[1:]
    num = len(argv)
    i = 1
    if num == 0:
        print("{:d} arguments.".format(num))
    elif num == 1:
        print("{:d} argument.".format(num))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments.".format(num))
        while i < num:
            print("{:d}: {:s}".format(i, sys.argv[i]))
            i += 1
