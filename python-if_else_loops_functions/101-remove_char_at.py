#!/usr/bin/env python3
def remove_char_at(str, n):
    if n > -1:
        str = str[0:n] + str[n + 1:len(str)]
    return str
