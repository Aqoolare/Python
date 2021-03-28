"""Скрипт для расчёта НОК

Функции:
    get_lcm(a, b): считает НОК
    get_gcf(a, b): считает НОД (для формулы НОК)
"""

import mypackage.core as pkg


def get_lcm(a, b):
    """Вычисляет наименьшее общее кратное для чисел a и b

    Аргументы:
        a (int): первое целое число
        b (int): второе целое число
    """
    flag = False
    if pkg.is_int(a) and pkg.is_int(b):
        a = abs(int(a))
        b = abs(int(b))
        if a != 0 and b != 0:
            print(f"НОК равен {int(a * b / get_gcf(a, b))}")
            flag = True
    if not flag:
        print(f"Введите ненулевые целые числа")

def get_gcf(a, b):
    """Возвращает наибольший общий делитель для чисел a и b

    Аргументы:
        a (int): первое целое число
        b (int): второе целое число

    Возвращает:
        int: наибольший общий делитель
    """
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == '__main__':
    a = input("Пожалуйста, введите целое число a: ")
    b = input("Пожалуйста, введите целое число b: ")
    get_lcm(a, b)