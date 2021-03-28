"""Скрипт, который убирает повторяющиеся элементы списка

Функции:
    select_elements(input_list): убирает повторяющиеся элементы списка
"""

def select_elements(input_list):
    """Выводит на экран список без повторяющихся элементов

    Аргументы:
        input_list (list): список, у которого необходимо 
        убрать повторяющиеся элементы
    """
    result_list = []
    for item in input_list:
        if item not in result_list:
            result_list.append(item)
    return result_list


if __name__ == '__main__':
    input_list = [i for i in \
        input("Пожалуйста, введите элементы списка через пробел:\n").split()]
    print(f"Оригинальный лист: {input_list}")
    print(f"Результирующий лист: {select_elements(input_list)}")