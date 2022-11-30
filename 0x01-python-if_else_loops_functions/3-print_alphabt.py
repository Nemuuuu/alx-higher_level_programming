#!/usr/bin/python3
c = "abcdefghijklmnopqrstuvwxyz"
for i in range(0,26):
    if c[i] == "e" or c[i] == "q":
        continue
    print(c[i], end="")
