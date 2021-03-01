"""
Задача
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Ссылка на диаграмму https://drive.google.com/file/d/1ymLinYYf49QkQpdEB1DY_ejyfRSZTyrd/view?usp=sharing
"""

n = int(input('Введите n элементов: '))
i = 0
range = 1
var_sum = 0
while i < n:
    var_sum += range
    range /= -2
    i += 1

print(f'Сумма {var_sum}')
