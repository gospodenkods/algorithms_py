# Условие
# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
# Ссылка на  блок схему  ниже
# https://drive.google.com/file/d/1IeV8YwdZF7VmN2ggF3yo1fwgI5soviDe/view?usp=sharing


a, b = input('Введите через пробел 2  буквы в латинском алфавите: ').split()

dif_a = ord(a) - ord('a') + 1
dif_b = ord(b) - ord('a') + 1

if a == b:
    distance = 0

else:
    distance = abs(dif_b - dif_a) - 1

print(f'Позиции введенных букв в алфавите: {dif_a} и {dif_b}')
print(f'Между этими буквами букв: {distance}')