"""Скрипт, который считает произвольный пример, введённый с клавиатуры

Функции:
    count_expression(input_expression): строит ОПЗ 
    и считает результат выражения
    count_from_opz(result_stack): по ОПЗ считает пример
"""

def count_expression(input_expression):
    """Строит обратную польскую запись выражния,
    затем считает по ней значение примера

    Аргументы:
        input_expression (str): строка-выражения, для которого
        будет построена ОПЗ

    Возвращает:
        float: значение примера
        или
        str: сообщение об ошибке
    """
    priority = {
        '(-)': 4,
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0}
    operations_stack = []
    result_stack = []
    end_index = len(input_expression) - 1
    start_index = 0
    error = False
    previous_symbol = ''
    error_message = '\n'
    while start_index <= end_index:
        if input_expression[start_index].isdigit():
            num = []
            while start_index <= end_index and \
                input_expression[start_index].isdigit():
                num.append(input_expression[start_index])
                start_index +=1
            start_index -= 1
            result_stack.append(''.join(num))
        elif input_expression[start_index] == '(':
            operations_stack.append('(')
        elif input_expression[start_index] == ')':
            if len(operations_stack) != 0:
                current_operation = operations_stack[-1]
            else:
                error = True
                error_message += "В выражении не согласованы скобки"
                break
            while current_operation != '(':
                result_stack.append(operations_stack.pop())
                if len(operations_stack) != 0:
                    current_operation = operations_stack[-1]
                elif current_operation != '(':
                    error_message += "В выражении не согласованы скобки"
                    error = True
                    break
            if len(operations_stack) != 0 and operations_stack[-1] == '(':
                operations_stack.pop()
        elif input_expression[start_index] in priority.keys():
            unary_minus = False
            if input_expression[start_index] == '-':
                if previous_symbol == '(' or previous_symbol == '':
                    operations_stack.append('(-)')
                    unary_minus = True
            if not unary_minus:
                if len(operations_stack) == 0 or \
                    priority[input_expression[start_index]] > \
                        priority[operations_stack[-1]]:
                    operations_stack.append(input_expression[start_index])
                elif priority[input_expression[start_index]] <= \
                    priority[operations_stack[-1]]:
                    current_operation = operations_stack[-1]
                    while priority[current_operation] >= \
                        priority[input_expression[start_index]]:
                        current_operation = operations_stack.pop()
                        result_stack.append(current_operation)
                        if len(operations_stack) > 0:
                            current_operation = operations_stack[-1]
                        else:
                            break
                    operations_stack.append(input_expression[start_index])
        else:
            error_message += "Неверный формат выражения"
            error = True
        if error:
            break
        previous_symbol = input_expression[start_index]
        start_index += 1
    if '(' in operations_stack:
        error_message += "В выражении не согласованы скобки"
        error = True
    if not error:    
        if start_index > end_index and len(operations_stack) != 0:
            while len(operations_stack) != 0:
                result_stack.append(operations_stack.pop())
        print(result_stack)
        return count_from_opz(result_stack)
    return error_message


def count_from_opz(result_stack):
    """Считает результат выражения, записанного в форме ОПЗ

    Аргументы:
        result_stack (list): список - обратная польская запись выражения

    Возвращает:
        float: результат вычисления
    """
    stack_for_count = []
    for item in result_stack:
        if item.isdigit():
            stack_for_count.append(int(item))
        else:
            if item == '(-)':
                a = stack_for_count.pop()
                stack_for_count.append(-a)
            elif item == '^':
                b = stack_for_count.pop()
                a = stack_for_count.pop()
                stack_for_count.append(a ** b)
            elif item == '*':
                b = stack_for_count.pop()
                a = stack_for_count.pop()
                stack_for_count.append(a * b)
            elif item == '/':
                b = stack_for_count.pop()
                a = stack_for_count.pop()
                stack_for_count.append(a / b)
            elif item == '+':
                b = stack_for_count.pop()
                a = stack_for_count.pop()
                stack_for_count.append(a + b)
            elif item == '-':
                b = stack_for_count.pop()
                a = stack_for_count.pop()
                stack_for_count.append(a - b)
    return f"{stack_for_count[0]:.2f}"
    
        
if __name__ == '__main__':
    # # Пример 1
    # expression = '(-5)^(-5+6)'
    # print(f"{expression}={count_expression(expression)}")

    # # Пример 2
    # expression = '(5+10)*(13-3)'
    # print(f"{expression}={count_expression(expression)}")

    # # Пример 3
    # expression = '(-10)^2'
    # print(f"{expression}={count_expression(expression)}")

    # # Пример 4
    # expression = '10+(30-25)*2'
    # print(f"{expression}={count_expression(expression)}")

    # # Пример 5
    # expression = '(-2)^(-1)'
    # print(f"{expression}={count_expression(expression)}")

    # #Пример 6
    # expression = '(-5)^((1+2)*(3-3))'
    # print(f"{expression}={count_expression(expression)}")

    # #Пример 7
    # expression = '((1+2)^2+2*10/2)^((1+2)*(3-1))'
    # print(f"{expression}={count_expression(expression)}")

    # #Пример 8
    # expression = '-((1+2)^2+2*10/2)^((1+2)*(3-2))'
    # print(f"{expression}={count_expression(expression)}")

    # expression = input("Пожалуйста, введите выражение для рассчёта: ")
    # print(f"{expression}={count_expression(expression)}")

    print(count_expression('-3+4*2/(1-5)^2'))