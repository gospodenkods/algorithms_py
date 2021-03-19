"""
Задача
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
меньше медианы, в другой — не больше медианы.
"""
import random


def mediana(in_array, i):
    if len(in_array) == 1:
        return in_array[0]

    trigger = random.choice(in_array)

    left_el = [el for el in in_array if el < trigger]
    right_el = [el for el in in_array if el > trigger]
    pivots = [el for el in in_array if el == trigger]

    if i < len(left_el):
        return mediana(left_el, i)
    elif i < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return mediana(right_el, i - len(left_el) - len(pivots))


MIN_ITEM = 0
MAX_ITEM = 50
MIN_SIZE = 5
MAX_SIZE = 10

m = random.randint(MIN_SIZE, MAX_SIZE)
size = 2 * m + 1
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(f'Исходный список:\n{array}')
print(f'Медианой списка является:\n{mediana(array, len(array) / 2)}')
array.sort()

print(f'Список после сортировки:\n{array}')
print(f'Медианой списка является:\n{array[len(array) // 2]}')
"""
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
sort_array = list(array)
print(f'Исходный список:\n{array}')
print(f'Медианой списка является:\n{mediana(array, len(array) / 2)}')
sort_array.sort()

print(f'Проверка!\nСписок после сортировки:\n{sort_array}')
print(f'Медианой списка является:\n{sort_array[len(sort_array) // 2]}')

if sort_array[len(sort_array) // 2] == mediana(array, len(array) // 2):
   print('\nВерно')
else:
   print('\nОшибка!!!')
"""
