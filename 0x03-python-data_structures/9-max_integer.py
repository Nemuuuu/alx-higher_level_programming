#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        i = 0
        max = my_list[i]
        while my_list[i + 1] > max:
            max = my_list[i]
            i += 1
    return max