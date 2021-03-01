# Задача
""" Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа
и знак операции вводятся пользователем. После выполнения вычисления программа не завершается, а
запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать
пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
Ссылка на диаграмму https://drive.google.com/file/d/1ymLinYYf49QkQpdEB1DY_ejyfRSZTyrd/view?usp=sharing
"""

while True:
    number1 = input('Введите число №1: ')
    number2 = input('Введите число №2: ')
    operation = input('Введите операнд: или 0 для выхода')
    if operation == '0':
        print('Выход из программы')
        break
    number1 = int(number1)
    number2 = int(number2)

    if operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')
