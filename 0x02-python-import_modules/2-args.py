#!/usr/bin/python3
import sys
if __name__ == '__name__':
    i = 1
    if i >= len(sys.argv):
        print("0 arguments.")
    else:
        while i <= len(sys.argv):
            if len(sys.argv) == 2:
                print("{} argument: ".format(len(sys.argv) - 1))
                print("{}: {}".format(i,sys.argv[i]))
            else:
                print("{} arguments: ".format(len(sys.argv) - 1))
                print("{}: {}".format(i,sys.argv[i]))
        i +=1
