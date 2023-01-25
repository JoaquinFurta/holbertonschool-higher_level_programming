#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lista = my_list.copy()
    for i in range(lista.count(search)):
        lista.insert(lista.index(search), replace)
        lista.remove(search)
    return lista
