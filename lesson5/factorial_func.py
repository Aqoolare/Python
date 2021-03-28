"""Скрипт вычисляет факториал числа

Функции:
    factorial(n): вычисляет факториал числа
"""

import mypackage.core as pkg
import mypackage311999.core as pkg1


def factorial(n):
    """Вычисляет факториал числа n

    Аргументы:
        n (int): число для вычисления факториала
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return(result)


if __name__ == '__main__':
    pkg1.safe_factorial(factorial) 

