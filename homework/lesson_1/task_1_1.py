# Условия
# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.
# Ссылка на  блок схему  ниже
# https://drive.google.com/file/d/1SYamNXh-fNAOIg6eMzCjLJ0WPoL2St8E/view?usp=sharing


input_var = int(input('Введите целое трехзначное число:'))

a = input_var // 100
b = (input_var // 10) % 10
c = input_var % 10

sum_var = a + b + c
comp = a * b * c

print(f'Сумма цифр в числе: {sum_var}')
print(f'Произведение цифр в числе: {comp}')
