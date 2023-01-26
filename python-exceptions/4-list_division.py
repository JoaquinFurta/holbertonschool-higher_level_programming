#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listdiv = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except (IndexError, RuntimeError):
            print("out of range")
            div = 0
        finally:
            listdiv.append(div)
    return(listdiv)
