"""
Задача
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

"""

import random

random_list = [random.randint(-10, 10) for _ in range(100)]
print(f'Массив в котором ищем : {random_list}')
min_index = 0

for i in random_list:
    if random_list[min_index] > i:
        min_index = random_list.index(i)

if random_list[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Минимальный отрицательный элемент: {random_list[min_index]},',
          f'индекс элемента {min_index}')
