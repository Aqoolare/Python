"""Скрипт для расчёта НОД

Функции:
    get_gcf(a, b): считает НОД
"""

import mypackage.core as pkg


def get_gcf(a, b):
    """Выводит на экран наибольший общий делитель для чисел a и b

    Аргументы:
        a (int): первое целое число
        b (int): второе целое число
    """
    flag = False
    if pkg.is_int(a) and pkg.is_int(b):
        a = abs(int(a))
        b = abs(int(b))
        if a != 0 and b != 0:
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            print(f"НОД равен {b}")
            flag = True
    if not flag:
        print("Введите целые числа не равные нулю")     


if __name__ == '__main__':
    a = input("Пожалуйста, введите целое число a: ")
    b = input("Пожалуйста, введите целое число b: ")
    get_gcf(a, b)