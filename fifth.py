# Создайте список с повторяющимися целыми числами
# Сформируйте список с порядковыми номерами нечетных элементов списка

my_tuple = (2, 3, 4, 8, 9, 9, 8, 7, 4, 2, 3, 1)
new_tuple = []
index = 1
for i, el in enumerate(my_tuple, 1):
    if el % 2 == 1:
        new_tuple.append(index)
    index += 1
print(new_tuple)