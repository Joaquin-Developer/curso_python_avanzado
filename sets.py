"""Ejemplos de la estructura set"""


def get_set():
    """obtenemos un set luego de aplicarle operaciones"""
    my_list = [1, 1, 2, 3, 4, 4]
    my_set = set(my_list)
    my_set.add(7)
    # añadir multiples elementos:
    my_set.update([4, 8, 9, 10])

    my_set.update({1, 12}, [20, 25])

    # Borrar elementos:
    # remove lanza error si intento borrar elementos inexistentes
    my_set.remove(2)
    # con discard, no obtenemos ese error
    my_set.discard(25)

    return my_set


def operaciones_con_set(my_set=None):
    set1 = {3, 4, 5}
    set2 = [5, 6, 7]

    # Union
    my_set_3 = set1 | set2 # {3,4,5,6,7}
    # Interseccion:
    my_set_4 = set1 & set2 # {5}
    # Diferencia:
    my_set_dif = set1 - set2
    # Dif simetrica:
    my_set_sim = set1 ^ set2 # {3,4,6,7}


def main():
    """main method"""
    pass

if __name__ == "__main__":
    main()
