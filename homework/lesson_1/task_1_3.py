# Условия
# По введенным пользователем координатам двух точек
# вывести уравнение прямой вида
# y = kx + b, проходящей через эти точки.
# Ссылка на  блок схему  ниже
# https://drive.google.com/file/d/1EVUigXhQb2PxQKifHWORAWA9rtoUWVM8/view?usp=sharing


x1, y1 = map(float, input('Задайте координаты первой точки через пробел: ').split())
x2, y2 = map(float, input('Задайте координаты первой точки через пробел: ').split())

a = y1 - y2
b = x2 - x1
c = x1 * y2 - x2 * y1
if a == 0 and b == 0:
    print('Точки совпадают')
elif a == 0:
    print(f'Уравнение прямой:\n'
          f'{b}y + {c} = 0')
elif b == 0:
    print(f'Уравнение прямой:\n'
          f'{a}x + {c} = 0')
else:
    print(f'Уравнение прямой:\n'
          f'{a}x + {b}y + {c} = 0')
