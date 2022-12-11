#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1 = list(set(set_1).difference(set_2))
    set2 = list(set(set_2).difference(set_1))
    r1 = set(set1)
    r2 = set(set2)
    return r1 | r2