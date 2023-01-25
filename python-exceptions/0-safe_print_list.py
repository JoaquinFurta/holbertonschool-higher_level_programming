#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
            if i == x:
                print()
                return i
        except IndexError:
            print()
            return i
