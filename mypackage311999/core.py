def count_chars_in_text(text):
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


def isPrime(number):
    flag = None
    if number.isdigit():
        number = int(number)
        if number > 1:
            border = int(number ** (1/2))
            for i in range(2, border + 1):
                if number % i == 0:
                    print("Это число составное")
                    flag = False
                    break
            if flag is None:
                print("Это число простое")
                flag = True
    if flag is None:
        print("Введите натуральное число больше 1")


def print_gcf(a, b):
    flag = False
    if is_int(a) and is_int(b):
        a = abs(int(a))
        b = abs(int(b))
        if a != 0 and b != 0:
            while a != b:
                if a > b:
                    a = a - b
                else:
                    b = b - a
            print(f"НОД равен {b}")
            flag = True
    if not flag:
        print("Введите целые числа не равные нулю")


def print_lcm(a, b):
    flag = False
    if is_int(a) and is_int(b):
        a = abs(int(a))
        b = abs(int(b))
        if a != 0 and b != 0:
            print(f"НОК равен {int(a * b / get_gcf(a, b))}")
            flag = True
    if not flag:
        print(f"Введите ненулевые целые числа")

def get_gcf(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def is_int(string_number):
    try:
        int(string_number)
        return True
    except ValueError:
        return False 

    
def safe_factorial(fact):
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