"""Скрипт для подсчёта частоты цифр в диапазоне чисел

Функции:
    count_digits_in_range(start, end): считает частоты цифр в диапазоне чисел
"""

import mypackage.core as pkg


def count_digits_in_range(start, end):
    """Считает количество цифр в заданном диапазоне

    Аргументы:
        start (int): значение начала диапазона
        end (int): значение конца диапазона
    """
    if pkg.is_int(start) and pkg.is_int(end):
        start = int(start)
        end = int(end)
        if start <= end:
            digits_frequency = {str(num): 0 for num in range(10)}
            for num in range(start, end + 1):
                num = str(num)
                for digit in num[1:]:
                    digits_frequency[digit] += 1
                if num[0] != '-':
                    digits_frequency[num[0]] += 1
            for key in digits_frequency.keys():
                print((f"Частота использования цифры "
                    f"'{key}': {digits_frequency[key]}"))
        else:
            print("Первое число должно быть не больше чем второе")
    else:
        print("Введите два целых числа")


if __name__ == '__main__':
    a = input("Пожалуйста, введите первое целое число a: ")
    b = input("Пожалуйста, введите второе целое число b: ")
    count_digits_in_range(a, b)