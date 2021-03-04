"""
Задача
Определить, какое число в массиве встречается чаще всего.

"""

import random

random_list = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {random_list}')

max_index = 0

for i in random_list:
    if random_list.count(max_index) < random_list.count(i):
        max_index = random_list.index(i)

print(f'Чаще всего встречается число {random_list.count(max_index)} ')
