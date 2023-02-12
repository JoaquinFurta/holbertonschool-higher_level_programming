#!/usr/bin/python3
""" function that returns a list of lists of integers
representing the Pascal’s triangle"""


def pascal_triangle(n):
    """ pascal """

    tri_l = []

    if n <= 0:
        return tri_l
    else:
        tri_l.append([1])
        tri_l.append([1, 1])

    for idx in range(1, n - 1):
        auxL = [1]
        for i in range(0, len(tri_l[idx]) - 1):
            x = tri_l[idx][i] + tri_l[idx][i + 1]
            auxL.append(x)

        auxL.append(1)
        tri_l.append(auxL)

    return tri_l
