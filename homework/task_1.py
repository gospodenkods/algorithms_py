"""
Задача
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Версия ОС
Windows 10 x64
Версия интерпритатора
Python 3.9.2


"""

import sys


def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


"""
Взял задачу 1 из первого  урока 
"""
input_var = int(input('Введите целое трехзначное число:'))

a = input_var // 100
b = (input_var // 10) % 10
c = input_var % 10

sum_var = a + b + c
comp = a * b * c

print(f'Сумма цифр в числе: {sum_var}')
print(f'Произведение цифр в числе: {comp}')

sum_member = sys.getsizeof(input_var) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + sys.getsizeof(
    sum_var) + sys.getsizeof(comp)

print('В программе задействовано байт памяти: {}'.format(sum_member))
"""

Введите целое трехзначное число:591
Сумма цифр в числе: 15
Произведение цифр в числе: 45
В программе задействовано байт памяти: 168

"""

"""
Взял задачу 8 из второго  урока 
Как  раз мне писали в комментариях на тему утечки памяти , вот  и охото посмотреть насколько память утекла
"""


def inputs(message):
    value = input(message + "\n")
    if not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        print('В программе задействовано байт памяти: {}'.format(show_size(value)))
        value = inputs(message)
    return value


input_range = input('Введите последовательность: ')
search_number = inputs('Введите цифру для поиска: ')
count = 0

for i in input_range:
    if i == search_number:
        count += 1

print(
    f'Цифра встречается {search_number} в последовательности {input_range}: \
{count} раз(а)'
)

sum_member = show_size(input_range)

print('В программе задействовано байт памяти: {}'.format(sum_member))

"""
Введите последовательность: 0001112223335555
Введите цифру для поиска: 
q
Вы ввели строку,а необходимо число 

 type=<class 'str'>, size=50, object=q
В программе задействовано байт памяти: 50
Введите цифру для поиска: 
w
Вы ввели строку,а необходимо число 

 type=<class 'str'>, size=50, object=w
В программе задействовано байт памяти: 50
Введите цифру для поиска: 
qwe
Вы ввели строку,а необходимо число 

 type=<class 'str'>, size=52, object=qwe
В программе задействовано байт памяти: 52
Введите цифру для поиска: 
5
Цифра встречается 5 в последовательности 0001112223335555: 4 раз(а)
 type=<class 'str'>, size=65, object=0001112223335555
В программе задействовано байт памяти: 65

"""

"""
Взял задачу 3 из третьего  урока 
Как  раз мне писали в комментариях на тему утечки памяти , вот  и охото посмотреть насколько память утекла
"""
import random

index_list = [random.randint(0, 99) for _ in range(10)]
print(f'Исходный массив: {index_list}')
sum_member = show_size(index_list)
print('В программе задействовано байт памяти: {}'.format(sum_member))
min_element = index_list[0]
max_element = index_list[0]

for i in index_list:
    if i < min_element:
        min_element = i
    elif i > max_element:
        max_element = i

min_index = index_list.index(min_element)
max_index = index_list.index(max_element)
index_list[min_index], index_list[max_index] = index_list[max_index], index_list[min_index]
print(f'Массив после замены {min_index} индексы {max_index}: {index_list}')
sum_member = show_size(index_list)
print('В программе задействовано байт памяти: {}'.format(sum_member))

"""
Размерность массивов идентично, что логично 

Исходный массив: [38, 30, 19, 8, 90, 18, 18, 54, 32, 27]
 type=<class 'list'>, size=184, object=[38, 30, 19, 8, 90, 18, 18, 54, 32, 27]
	 type=<class 'int'>, size=28, object=38
	 type=<class 'int'>, size=28, object=30
	 type=<class 'int'>, size=28, object=19
	 type=<class 'int'>, size=28, object=8
	 type=<class 'int'>, size=28, object=90
	 type=<class 'int'>, size=28, object=18
	 type=<class 'int'>, size=28, object=18
	 type=<class 'int'>, size=28, object=54
	 type=<class 'int'>, size=28, object=32
	 type=<class 'int'>, size=28, object=27
В программе задействовано байт памяти: 464
Массив после замены 3 индексы 4: [38, 30, 19, 90, 8, 18, 18, 54, 32, 27]
 type=<class 'list'>, size=184, object=[38, 30, 19, 90, 8, 18, 18, 54, 32, 27]
	 type=<class 'int'>, size=28, object=38
	 type=<class 'int'>, size=28, object=30
	 type=<class 'int'>, size=28, object=19
	 type=<class 'int'>, size=28, object=90
	 type=<class 'int'>, size=28, object=8
	 type=<class 'int'>, size=28, object=18
	 type=<class 'int'>, size=28, object=18
	 type=<class 'int'>, size=28, object=54
	 type=<class 'int'>, size=28, object=32
	 type=<class 'int'>, size=28, object=27
В программе задействовано байт памяти: 464


"""