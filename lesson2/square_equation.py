"""Скрипт для решения квадратного уравнения

Функции:
    solve_square_equation(a, b, c): - решает квадратное уравнение 
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
    if a:
        double_a = 2 * a
        d_sqrt = cmath.sqrt(b**2 - 4*a*c)
        z1 = (-b + d_sqrt) / double_a
        z2 = (-b - d_sqrt) / double_a
        print(f"Ответ: {z1}, {z2}")
    elif b:
        print(f"Ответ: {-c / b}")
    elif not c:
        print("Решениями являются любые комплексные (и действительные) числа")
    else:
        print(f"Пожалуйста, введите корректные коэффициенты")


if __name__ == '__main__':
    #Пример 1
    print("Пример 1. Коэффициенты: 1; -7+2j; 13-13j")
    solve_square_equation(complex("1"), complex("-7+2j"), complex("13-13j"))
    #Пример2
    print("Пример 2. Коэффициенты: 3; 7; -6")
    solve_square_equation(complex("3"), complex("7"), complex("-6"))
    #Пример3
    print("Пример 3. Коэффициенты: 1; -6; 13")
    solve_square_equation(complex("1"), complex("-6"), complex("13"))


    print("Пожалуйста, введите коэффициенты квадратного уравнения "
    "(в случае комплексных коэффициентов в качестве мнимой единцы "
    "используется j):")
    a = input("Пожалуйста, введите коэффициент a:\n")
    b = input("Пожалуйста, введите коэффициент b:\n")
    c = input("Пожалуйста, введите коэффициент c:\n")
    solve_square_equation(complex(a), complex(b), complex(c))