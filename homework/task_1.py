""""
Задача

Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
 [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не иду
"""

import random


def sort(input_array, trigger=False):
    if trigger:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    length = len(input_array)
    while n < length:
        count = True
        for i in range(n - 1, length - n):
            if input_array[i + left] > input_array[i + right]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
                count = False
        if count:
            break
        for j in range(length - n, n - 1, -1):
            if input_array[j - left] < input_array[j - right]:
                input_array[j], input_array[j - 1] = input_array[j - 1], input_array[j]
        n += 1


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
random.shuffle(array)
print(f'Массив до сортировки:\n{array}')
sort(array, trigger=True)
print(f'Массив после сортировки:\n{array}')
