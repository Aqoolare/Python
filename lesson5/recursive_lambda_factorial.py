import mypackage.core as pkg
import mypackage311999.core as pkg1


"""Нерекурсивная анонимная функция для расчёта факториала числа"""
fact = lambda n: n*fact(n-1) if n > 0 else 1

if __name__ == '__main__':
    pkg1.safe_factorial(fact)