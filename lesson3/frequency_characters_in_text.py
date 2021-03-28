"""Скрипт для подсчёта частоты символов в тексте

Функции:
    count_chars_in_text(text): считает частоты символов в тексте
"""

def count_chars_in_text(text):
    """Выводит на экран количество символов в строке,
    поступившей в качестве параметра

    Аргументы:
        text (str): строка, для которой нужно посчитать
        количество символов
    """
    char_dict = {}
    for char in text:
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict.update({char: 1})
    list_keys = list(char_dict.keys())
    list_keys.sort()
    for key in list_keys:
        print(f"Частота символа '{key}': {char_dict[key]}")


if __name__ == '__main__':
    text = input("Введите текст: \n")
    count_chars_in_text(text)