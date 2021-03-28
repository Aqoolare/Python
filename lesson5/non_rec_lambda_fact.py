import operator
from functools import reduce

import mypackage.core as pkg
import mypackage311999.core as pkg1


"""Нерекурсивная анонимная функция для расчёта факториала числа"""
fact = lambda n: reduce(operator.mul, [i for i in range(1, n + 1)])


if __name__ == '__main__':
    pkg1.safe_factorial(fact)