#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    iterr = 0
    nb_print = iterr
    while True:
        try:
            if iterr == x:
                print()
                return nb_print
            print("{:d}".format(my_list[iterr]), end="")
            iterr += 1
            nb_print += 1
        except (TypeError, ValueError):
            iterr += 1
