"""Скрипт, который проверяет правильность расстановки скобок в строке

Функции:
    check_parentheses(input_string): проверяет, правильно ли 
    расставлены скобки
"""

def check_parentheses(input_string):
    """Проверяет правильность растановки скобок в строке,
    выводит ответ на экран

    Аргументы:
        input_string (str): строка, содержащая скобки
    """
    parentheses_stack = []
    start_index = 0
    error = False
    end_index = len(input_string) - 1
    open_parentheses = {')':'(', ']':'[', '}':'{'}
    error_message = "В выражении не согласованы скобки"
    while start_index <= end_index:
        if input_string[start_index] in open_parentheses.values():
            parentheses_stack.append(input_string[start_index])
        elif input_string[start_index] in open_parentheses.keys():
            if len(parentheses_stack) != 0:
                current_operation = parentheses_stack[-1]
            else:
                error = True
                break
            if current_operation == \
                open_parentheses[input_string[start_index]]:
                parentheses_stack.pop()
            else:
                error = True
                break
        start_index += 1
    if set(open_parentheses.values()).intersection(set(parentheses_stack)):
        error = True
    if error:
        return error_message
    else:
        return "Скобки расставлены правильно"


if __name__ == '__main__':
    print(check_parentheses(input("Введите выражение со скобками:\n")))