"""
- Ejemplo de generadores
- Generadores == Iteradores pero con una sintaxis mas agradable
"""


def my_gen():
    """un ejemplo de generadores"""
    print("Hola mundo")
    n = 0
    yield n

    print("Hola de nuevo!")
    n = 1
    yield n

    print("De nuevo... holis")
    n = 2
    yield n


def generator_example():
    """diferencias entre l_c y generator"""
    my_list = [0, 1, 4, 7, 9, 10]
    # List comprehension:
    my_second_list = [x*2 for x in my_list]
    # Generator expression:
    my_second_gen = (x*2 for x in my_list)


def main():
    """main function"""
    a = my_gen() # objeto de tipo generador
    # next nos lleva al yield mas próximo
    print(next(a))
    print(next(a))
    print(next(a))
    # print(next(a)) # StopIteration exception


if __name__ == "__main__":
    main()
