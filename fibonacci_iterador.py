"""EJemplo de Fibonacci con iterador"""
import time


class FiboIter:
    """representación de los objetos de tipo iterador"""

    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.num1
        elif self.counter == 1:
            self.counter += 1
            return self.num2
        
        self.aux = self.num1 + self.num2
        self.num1, self.num2 = self.num2, self.aux
        self.counter += 1
        return self.aux


def main():
    """main function"""
    fib = FiboIter()
    for element in fib:
        print(element)
        if fib.counter > 10:
            break

if __name__ == "__main__":
    main()
