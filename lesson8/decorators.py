import time


def time_decorator(function_to_decorate):
    def func(*args):
        ts = time.time()
        res = function_to_decorate(*args)
        print(f"Время выполнения функции {time.time() - ts:.2f}")
        return res
    return func


def logging_decorator(function_to_decorate):
    def func(*args):
        res = function_to_decorate(*args)
        print(f"Функция вызвана с аргументами {args}")
        return res
    return func


def counter_decorator(function_to_decorate):
    def func(*args):
        func.count += 1
        res = function_to_decorate(*args)
        print(f"Функция вызвана {func.count} раз(a)")
        return res
    func.count = 0
    return func



@counter_decorator
@logging_decorator
@time_decorator
def factorial(n):
    result = 1
    while n > 1:
        time.sleep(0.1)
        result *= n
        n -= 1
    return result


if __name__ == "__main__":
    factorial(5)
    factorial(7)
    factorial(10)

