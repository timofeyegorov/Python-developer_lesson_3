elements_1 = input('Введите элементы списка 1 через запятую: ')
elements_2 = input('Введите элементы списка 2 через запятую: ')

spisok_1 = set(elements_1.split(','))
spisok_2 = set(elements_2.split(','))

print(spisok_1.difference(spisok_2))