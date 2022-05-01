"""EJemplo de Fibonacci con iterador"""
import time


class FiboIter:
    """representación de los objetos de tipo iterador"""

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num1 = 0
        self.num2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.counter <= self.max:
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

        raise StopIteration

def main():
    """main function"""
    fib = FiboIter(max=8)
    for element in fib:
        print(element)
        time.sleep(0.70)

if __name__ == "__main__":
    main()
