"""Скрипт реализующий мехаинзм копилки с процентной ставкой

Функции:
    total_amount_calc(monthly_amount, interest, months_number): реализует
    алгоритм расчёта количества денег спустя несколько месяцев
"""

def total_amount_calc(monthly_amount, interest, months_number):
    """Считает, сколько будет денег через определённое количество
    месяцев с определённой процентной ставкой, с определённой
    величиной ежемесячного взноса

    Args:
        monthly_amount (float): 
        interest ([type]): [description]
        months_number ([type]): [description]
    """
    total_amount = 0
    interest /= 100
    for i in range(1, months_number + 1):
        total_amount += monthly_amount
        total_amount *= (1 + interest)
    print(f'{total_amount:.2f}')


if __name__ == '__main__':
    flag1, flag2 = False, False
    while True:
        if not flag1:
            message = ("Пожалуйста, введите ежемесячный взнос "
            "(Enter - чтобы выйти): ")
            monthly_amount = input(message)
            if not monthly_amount:
                break
            try:
                monthly_amount = float(monthly_amount)
            except ValueError:
                print("Пожалуйста, введите число больше нуля")
                continue
            if monthly_amount <= 0:
                print("Пожалуйста, введите число больше нуля")
                continue
            else:
                flag1 = True
        if not flag2:
            interest = input("Пожалуйста, введите количество % "
            "(Enter - чтобы начать заново): ")
            if not interest:
                flag1, flag2 = False, False
                continue
            try:
                interest = float(interest)
            except ValueError:
                print("Пожалуйста, введите неотрицательное число")
                continue
            if interest < 0:
                print("Пожалуйста, введите неотрицательное число")
                continue
            else:
                flag2 = True   
        months_number = input("Пожалуйста, "
        "количество месяцев (Enter - чтобы начать заново): ")
        if not months_number:
            flag1, flag2 = False, False
            continue
        try:
            months_number = int(months_number)
        except ValueError:
            print("Пожалуйста, введите натуральное число")
            continue
        if months_number <= 0:
            print("Пожалуйста, введите натуральное число")
            continue
        total_amount_calc(monthly_amount, interest, months_number)
        flag1, flag2 = False, False
