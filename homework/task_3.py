"""
Задача
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

Мы помним об ограничениях на max, min, sum, sorted!!!!
"""


import random

index_list = [random.randint(0, 99) for _ in range(10)]
print(f'Исходный массив: {index_list}')

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