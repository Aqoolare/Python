"""Скрипт реализующий частотный анализ текста,
вычиляющий количество слов и предложений в тексте

Функции:
    count_words_in_text(text): вычисляет количество слов в тексте
    count_sentences_in_text(text): вычисляет количество предложений в тексте
    
    функция частотного анализа импортируется 
    из модуля frequency_characters_in_text
"""

import re

import mypackage.core as pkg
import mypackage311999.core as pkg1


def count_words_in_text(text):
    """Посчитать количество слов в тексте и вывести результат на экран

    Аргументы:
        text (str): текст, для которого нужно посчитать количество слов
    """
    result = re.findall(r'\w+', text)
    print(f"Количество слов в тексте: {len(result)}")


def count_sentences_in_text(text):
    """Посчитать количество предложений в тексте и вывести результат на экран

    Аргументы:
        text (str): текст, для которого нужно посчитать количество предложений
    """
    result = re.split(r'[.?!]\s', text)
    print(f"Количество предложений в тексте: {len(result)}")


if __name__ == '__main__':
    state = 'input text'
    while True:
        if state == 'input text':
            text = input("Введите текст (Enter - чтобы выйти):\n")
            if not text:
                break
        case = input(("Введите код операции (1, 2, 3) " 
        "Enter - чтобы вернуться к набору текста:\n"))
        if case == '1':
            pkg1.count_chars_in_text(text)
            state = 'input op'
        elif case == '2':
            count_words_in_text(text)
            state = 'input op'
        elif case == '3':
            count_sentences_in_text(text)
            state = 'input op'
        elif case == '':
            state = 'input text'
        else:
            state = 'input op'
            print("***Пожалуйста, введите корректный код операции***")


