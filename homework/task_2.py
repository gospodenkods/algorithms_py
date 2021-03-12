"""
Задача
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict
from collections import deque


def to_hex(n):
    num_list = deque()
    while n > 0:
        d = n % 16
        for i in count_:
            if count_[i] == d:
                num_list.append(i)
        n //= 16
    num_list.reverse()
    return list(num_list)


def to_dec(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += count_[num[i]] * 16 ** i
    return dex


chars = '0123456789ABCDEF'
count_ = defaultdict(int)
counter = 0
for key in chars:
    count_[key] += counter
    counter += 1

num_1 = to_dec(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
num_2 = to_dec(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {to_hex(num_1 + num_2)}')
print(f'Произведение чисел: {to_hex(num_1 * num_2)}')
