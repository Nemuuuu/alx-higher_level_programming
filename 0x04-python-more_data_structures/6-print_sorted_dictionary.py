#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.items())
    for i,srt in sorted_dic:
        print("{}: {}".format(i,srt))