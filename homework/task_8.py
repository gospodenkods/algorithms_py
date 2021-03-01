"""
Задача
Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры.
Ссылка на диаграмму https://drive.google.com/file/d/1ymLinYYf49QkQpdEB1DY_ejyfRSZTyrd/view?usp=sharing
"""


def inputs(message):
    value = input(message + "\n")
    if not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        value = inputs(message)
    return value


input_range = input('Введите последовательность: ')
search_number = inputs('Введите цифру для поиска: ')
count = 0

for i in input_range:
    if i == search_number:
        count += 1

print(
    f'Цифра встречается {search_number} в последовательности {input_range}: \
{count} раз(а)'
)
