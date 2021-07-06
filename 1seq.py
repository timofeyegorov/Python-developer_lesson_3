spisok = []
len_list = int(input('Введите кол-во элементов списка: '))
for i in range(len_list):
    spisok.append(input(f'Введите число {i+1}: '))
print(spisok)