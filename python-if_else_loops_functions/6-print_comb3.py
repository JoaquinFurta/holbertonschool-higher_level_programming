#!/usr/bin/python3
for i in range(0, 9):
    for x in range(1, 10):
        if x != i and i < x:
            print("{}{}".format(i, x), end=", ")
print()
