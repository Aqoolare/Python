"""Скрипт реализующий обработку пользовательского ввода
для расчёта факториала

Функции:
    safe_factorial(fact): алгортим взаимодействия с пользователем
    для расчёта факториала
"""

def safe_factorial(fact):
    """Обработка пользовательского ввода и расчёт факториала с выводом
    результата на экран
    
    Аргументы:
    fact (анонимная функция): вычисляет факториал
    """
    while True:
        n = input("Введите число для расчёта факториала "
        "(Enter - чтобы выйти): ")
        if not n:
            break
        try:
            n = int(n)
        except ValueError:
            print("Введите неотрицательное целое число")
        else:
            if n >= 0:
                result = fact(n)
                print(f"Факториал числа равен: {result}")
            else:
               print("Целое число должно быть неотрицательным")