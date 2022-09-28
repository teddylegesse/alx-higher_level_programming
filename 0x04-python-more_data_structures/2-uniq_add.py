#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_of_unique_numbers = set(my_list)
    add = 0

    for i in list_of_unique_numbers:
        add += i

    return (add)
