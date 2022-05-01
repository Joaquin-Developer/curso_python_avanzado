"""remove duplicates module"""
from typing import List


def _remove_duplicates(some_list: List) -> List:
    """A partir de una lista, retornamos una lista con
    los mismos elementos pero sin los repetidos.
    Algoritmo sin usar set"""
    without_duplicates = []
    for elem in some_list:
        if elem not in without_duplicates:
            without_duplicates.append(elem)
    return without_duplicates


def remove_duplicates(some_list: List) -> List:
    """A partir de una lista, retornamos una lista con
    los mismos elementos pero sin los repetidos"""
    return list(set(some_list))
