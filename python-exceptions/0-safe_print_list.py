#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            if i == x:
                print()
                return i

            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            print()
            return i
