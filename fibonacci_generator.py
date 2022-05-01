"""Sucesion de fibo con Generator"""
import time


def fibo_gen(tope=None):
    """fibonacci con generadores"""
    num1, num2, counter = 0, 1, 0

    while True:
        if counter == 0:
            counter += 1
            yield num1
        elif counter == 1:
            counter += 1
            yield num2

        aux = num1 + num2
        if not tope or counter < tope:
            num1, num2 = num2, aux
            counter += 1
            yield aux
        else:
            break


def main():
    """main function"""
    fibonacci = fibo_gen(tope=8)
    for element in fibonacci:
        print(element)
        time.sleep(1)


if __name__ == "__main__":
    main()
