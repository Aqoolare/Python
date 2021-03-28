"""Скрипт для решения квадратного уравнения

Функции:
    solve_square_equation(a, b, c): решает квадратное уравнение
    is_complex(string_number): проверяет, является ли строка 
    комплексным числом
"""

import cmath


def solve_square_equation(a, b, c):
    """По заданным коэфициентам квадратного уравнения
    выводит на экран его корни

    Аргументы:
        a (complex): коэфициент при x в квадрате
        b (complex): коэфициент при x
        c (complex): свободный член уравнения
    """
    if is_complex(a) and is_complex(b) and is_complex(c):
        a = complex(a)
        b = complex(b)
        c = complex(c)
        if a:
            double_a = 2 * a
            d_sqrt = cmath.sqrt(b**2-4*a*c)
            z1 = (-b + d_sqrt) / double_a
            z2 = (-b - d_sqrt) / double_a
            print(f"Ответ: {z1:.2f}, {z2:.2f}")
        elif b:
            print(f"Ответ: {-c / b:.2f}")
        elif not c:
            print("Решениями являются любые комплексные " 
            "(и действительные) числа")
        else:
            print(f"Пожалуйста, введите корректные коэффициенты")
    else:
        print(f"Пожалуйста, введите корректные коэффициенты")

def is_complex(string_number):
    """Проверяет, является ли строка комплексным числом            

    Аргументы:
        string_number (str): строка для проверки на комплексное число

    Возвращает:
        bool: является ли число комплексным
    """
    try:
        complex(string_number)
        return True
    except ValueError:
        return False  


if __name__ == '__main__':
    #Пример 1
    print("Пример 1. Коэффициенты: 1; -7+2j; 13-13j")
    solve_square_equation("1", "-7+2j", "13-13j")
    #Пример2
    print("Пример 2. Коэффициенты: 3; 7; -6")
    solve_square_equation("3", "7", "-6")
    #Пример3
    print("Пример 3. Коэффициенты: 1; -6; 13")
    solve_square_equation("1", "-6", "13")


    print("Пожалуйста, введите коэффициенты квадратного уравнения "
    "(в случае комплексных коэффициентов в качестве мнимой единцы "
    "используется j):")
    a = input("Пожалуйста, введите коэффициент a:\n")
    b = input("Пожалуйста, введите коэффициент b:\n")
    c = input("Пожалуйста, введите коэффициент c:\n")
    solve_square_equation(a, b, c)