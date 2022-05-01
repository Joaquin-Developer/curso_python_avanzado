"""Decoradores"""
from datetime import datetime


def execution_time(func):
    """
    - determinar cuanto tiempo tarda en ejecutarse una funcion
    - recibe una funcion como parametro
    """
    def wrapper(*args, **kwargs):
        """envoltura"""
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {str(time_elapsed.total_seconds())} segundos")
    return wrapper


@execution_time
def random_func():
    """for con 1M repeticiones"""
    for _ in range(1, 1000000):
        pass


@execution_time
def suma(num1: int, num2: int) -> int:
    """suma de dos enteros"""
    return num1 + num2


@execution_time
def saludo(nombre: str = "Joaquin") -> None:
    """saludar"""
    print("Hola " + nombre)

if __name__ == "__main__":
    # random_func()
    suma(5, 5)
    saludo()
    