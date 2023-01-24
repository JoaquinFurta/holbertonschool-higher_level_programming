#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
       for i in matrix:
            list(map(lambda i:print("{:d}".format(i),end=" "), i))
            print() 
