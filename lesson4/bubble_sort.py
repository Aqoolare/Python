"""Скрипт для выполнения сортировки пузырьком

Функции:
    bubble_sort(list): сортирует список
"""

def bubble_sort(list):
    """Сортирует список сортировкой пузырьком

    Аргументы:
        list (list): список для сортировки
    """
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


if __name__ == '__main__':
    try:
        list = [int(i) for i in \
            input("Пожалуйста, введите элементы через пробел:\n").split()]
        bubble_sort(list)
        print(f"Отсортированный лист: {list}")
    except ValueError:
        print("Введены некорректные данные")