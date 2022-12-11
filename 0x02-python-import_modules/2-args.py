#!/usr/bin/python3
import sys
if __name__ == '__name__':
    i = 1
    if i >= len(sys.argv):
        print(f"0 arguments.")
    else:
        while i >= len(sys.argv):
            if len(sys.argv) == 2:
                print(f"{len(sys.argv) - 1} argument: ")
                print(f"{i}: {sys.argv[i]}")
            else:
                print(f"{len(sys.argv) - 1} arguments: ")
                print(f"{i}: {sys.argv[i]}")
        i +=1
