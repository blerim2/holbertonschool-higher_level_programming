#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum([x for i, x in enumerate(my_list) if x not in my_list[:i]])
