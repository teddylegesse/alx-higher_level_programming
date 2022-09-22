#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num = len(argv) - 1
    if num == 0:
        print("{}".format(num))
    else:
        result = []
        for i in range(1, num + 1):
            result.append(int(argv[i]))
        print("{}".format(sum(result))
