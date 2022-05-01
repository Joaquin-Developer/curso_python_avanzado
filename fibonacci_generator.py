"""Sucesion de fibo con Generator"""
import time


def fibo_gen():
    """fibonacci con generadores"""
    num1 = 0
    num2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield num1
        elif counter == 1:
            counter += 1
            yield num2
        aux = num1 + num2
        num1, num2 = num2, aux
        counter += 1
        yield aux


def main():
    """main function"""
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)


if __name__ == "__main__":
    main()
