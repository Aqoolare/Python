"""Скрипт для определения, явлется ли строка целым числом

Функции:
    is_int(string_number): определяет, явлется ли строка целым числом
"""

def is_int(string_number):
    """Проверяет, является ли строка целым числом            

    Аргументы:
        string_number (str): строка для проверки на целое число

    Возвращает:
        bool: является ли число целым
    """
    try:
        int(string_number)
        return True
    except ValueError:
        return False 