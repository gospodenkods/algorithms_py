"""
Задача
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def sort(arr):

    def merge(first, last):
        result = []
        i, n = 0, 0

        while i < len(first) and n < len(last):

            if first[i] < last[n]:
                result.append(first[i])
                i += 1

            else:
                result.append(last[n])
                n += 1

        result.extend(first[i:] if i < len(first) else last[n:])

        return result

    def div_half(lst):

        if len(lst) == 1:
            return lst

        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]

        else:
            return merge(div_half(lst[:len(lst)//2]), div_half(lst[len(lst)//2:]))

    return div_half(arr)


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив до сортировки:\n{array}')
print(f'Массив после сортировки:\n{array}')