"""Iterador"""


def iterando_iterador():
    """iterar un ietrador de una forma fea xd, con iter"""
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)

    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break


def iterador_for():
    """iterador de forma mas simple con for"""
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(element)


def main():
    """main function"""
    iterando_iterador()
    iterador_for()


class EventNumbers:
    """
    clase que implementa un iterador de todos los numeros pares,
    o los números pares hasta un máximo
    """

    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        raise StopIteration


if __name__ == "__main__":
    main()
    