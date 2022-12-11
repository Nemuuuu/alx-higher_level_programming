#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = [num for num in my_list if my_list.count(num) > 1]
    duplic = list(set(uniq))
    unique = list(set(my_list))
    sum = 0
    for i in unique:
        sum += i
        
    return sum