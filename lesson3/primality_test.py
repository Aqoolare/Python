"""Скрипт для поверки числа на простоту

Функции:
    isPrime(number): определяет, является ли число простым
"""

import math

def isPrime(number):
    """Выводит на экран ответ, является ли число простым

    Args:
        number (int): число для проверки на простоту
    """
    flag = None
    if number.isdigit():
        number = int(number)
        if number > 1:
            border = int(math.sqrt(number))
            for i in range(2, border + 1):
                if number % i == 0:
                    print("Это число составное")
                    flag = False
                    break
            if flag is None:
                print("Это число простое")
                flag = True
    if flag is None:
        print("Введите натуральное число больше 1")


if __name__ == '__main__':
    number = input("Пожалуйста, введите натуральное число больше единицы: ")
    isPrime(number)