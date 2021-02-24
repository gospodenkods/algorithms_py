# Условия
# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.
# Ссылка на  блок схему  ниже
# https://drive.google.com/file/d/1E4-uVgKPujyqTbA1K0J_uY_3rNLteJv-/view?usp=sharing

a = int(input('Введите порядковый номер буквы: '))

a += ord('a') - 1

b = chr(a)

print(f'Ваша буква: {b}')
