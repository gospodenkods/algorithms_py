"""
Задача
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

import collections
import sys

# Ругались как  то на утечку памяти
while True:
    try:
        input_int = int(input('Сколько компаний участвуют в расчете ? Введине 0 для выхода из программы: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

enterprises = collections.defaultdict()
profit_ = collections.deque()
un_profit = collections.deque()
all_profit = 0
QUARTER = 4

for i in range(input_int):
    name = input(f'\nВведите название {i + 1}й компании: ')
    if name == 0:
        break

    profit = 0
    quarter_count = 1
    while quarter_count <= QUARTER:
        try:
            profit += float(input(f'Введите прибыль за {quarter_count}й квартал: '))
        except ValueError:
            print('Вы ввели строку или спец символ')
            continue
        quarter_count += 1
    enterprises[name] = profit
    all_profit += profit
if input_int == 0:
    sys.exit()
midle_profit = all_profit / input_int
for i, item in enterprises.items():
    if item >= midle_profit:
        profit_.append(i)
    else:
        un_profit.append(i)
print(f'Средняя прибыль  составила: {midle_profit}')
print(f'Прибыль выше у {len(profit_)} компаний:')
for name in profit_:
    print(name)
print(f'Прибыль ниже у {len(un_profit)} компаний:')
for name in un_profit:
    print(name)
