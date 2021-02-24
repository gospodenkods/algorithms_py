# Условие
# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого)
# Ссылка на  блок схему  ниже
# https://drive.google.com/file/d/1N3mSqrBl1tPgmeLde_Et6gbZKQVsdiFO/view?usp=sharing

n1, n2, n3 = [x for x in input('Введите три числа, через пробел: ').split()]

if n2 < n1 < n3 or n3 < n1 < n2:
    print(f'Среднее: {n1}')
elif n1 < n2 < n3 or n3 < n2 < n1:
    print(f'Среднее: {n2}')
else:
    print(f'Среднее: {n3}')
