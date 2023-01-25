#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i ** 2 for i in elem] for elem in matrix]

    '''This would do the same but using map function
        lista = []
        for element in matrix:
            lista.extend([list(map(lambda i: i ** 2, element))])
        return lista '''
