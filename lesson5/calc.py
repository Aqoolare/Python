"""Скрипт реализует калькулятор для базовых бинарных опеаций

Функции:
    calc(a=1, b=2, operation='+'): вычисляет операцию
    do_calc(): реализует логику работы калькулятора
"""

import time


def calc(a=1, b=2, operation='+'):
    """В зависимости от значения операции возвращает результат её выполнения

    Аргументы:
        a (int, optional): первый аргумент. По умолчанию 1.
        b (int, optional): второй аргумент. По умолчанию 2.
        operation (str, optional): строка-значение операции. По умолчанию '+'.

    Возвращает:
        float: результат выполнения операции
    """
    def add(a1, b1):
        """Выполняет сложение двух элементов

        Аргументы:
            a1 (float): первый аргумент
            b1 (float): второй аргумент

        Возвращает:
            float: результат сложения
        """
        return a1 + b1
    
    def remove(a1, b1):
        """Выполняет вычитание элемента b1 из элемента a1

        Аргументы:
            a1 (float): первый аргумент
            b1 (float): второй аргумент

        Возвращает:
            float: результат вычитания
        """
        return a1 - b1
    
    def multiply(a1, b1):
        """Выполняет умножение элемента a1 на элемент b1

        Аргументы:
            a1 (float): первый аргумент
            b1 (float): второй аргумент

        Возвращает:
            float: результат умножения
        """
        return a1 * b1
    
    def divide(a1, b1):
        """Выполняет деление элемента a1 на элемент b1

        Аргументы:
            a1 (float): первый аргумент
            b1 (float): второй аргумент

        Возвращает:
            float: результат деления
        """
        return a1 / b1

    def pow(a1, b1):
        """Выполняет возведение элемента a1 в степень b1

        Аргументы:
            a1 (float): первый аргумент
            b1 (float): второй аргумент

        Возвращает:
            float: результат возведения в степень
        """
        return a1 ** b1

    selector = {'+': add, '-': remove, '*': multiply, '/': divide, '^': pow}
    return selector[operation](a, b)

def do_calc():
    """Эмулирует работу калькулятора
    """
    cur_value, b = 0, 0
    current_state = ''
    ops = {'+', '-', '/', '*', '^'}
    op = ''
    print("Запуск калькулятора...")
    time.sleep(0.5)
    print("Калькулятор запущен (Enter - чтобы выйти)")
    while True:
        if current_state == '':
            try:
                input_value = input("Введите первый агрумент: ")
                if not input_value:
                    break
                else:
                    cur_value = float(input_value)
            except ValueError:
                print("Пожалуйста, введите число")
            else:
                current_state = 'a'
        if current_state == 'a':
            op = input("Введите операцию (+, -, *, /, ^): ")
            if not op:
                break
            elif op not in ops:
                print('Пожалуйста, введите корректный значок операции')
            else:
                current_state = 'o'
        if current_state == 'o':
            try:
                input_value = input("Введите второй агрумент: ")
                if not input_value:
                    break
                else:
                    b = float(input_value)
            except ValueError:
                print("Пожалуйста, введите число")
            else:
                try:
                    cur_value = calc(cur_value, b, op)
                except ZeroDivisionError:
                    cur_value = float('inf')
                except OverflowError:
                    cur_value = float('nan')
                finally:
                    print(f"Текущее значение: {cur_value}")
                    current_state = 'a'


if __name__ == '__main__':
    do_calc()