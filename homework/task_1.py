"""
Задача
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""


import hashlib


def decompose_sub(s):
    first = []
    last = []

    for len_ in range(1, len(s)):
        for i in range(len(s) - len_ + 1):
            h_sub = hashlib.sha1(s[i:i + len_].encode('utf-8')).hexdigest()
            if h_sub not in first:
                first.append(h_sub)
                last.append(s[i:i + len_])

    if len(last) > 0:
        return f'В строке "{s}" найдено {len(last)} уникальных подстрок: \n{last}'
    return 'Пустая строка'


input_str = input('Введите строку: ')
print(decompose_sub(input_str))
