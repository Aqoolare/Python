"""Скрипт для решения задачи FizzBuzz

Функции:
    fizzbuzz(): - решает задачу FizzBuzz
"""


def fizzbuzz():
    """Решает задачу FizzBuzz,
    выводит на экран результат
    """
    result = []
    for number in range(1, 101):
        if number % 15 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(number))
    print(' '.join(result))


if __name__ == '__main__':
    fizzbuzz() 