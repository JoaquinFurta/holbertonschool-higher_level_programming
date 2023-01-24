#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
       for i in matrix:
           print("{:s}".format(' '.join(map(str, i))))
