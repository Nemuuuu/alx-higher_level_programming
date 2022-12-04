#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    j = 0
    while j < len(my_list):
        if my_list[j] % 2 == 0:
            res = my_list[j]
            j += 1
            return res