# Дан список повторяющихся элементов. Вернуть список с дублирующими
# элементами. В результирующем списке не должно быть дубликатов

my_list = [1, 2, 3, 5, 5, 5, 5, 3, 4, 0, 0, 6, 9, 1]

new_list = []

for i in my_list:
    if my_list.count(i) > 1 and i not in new_list:
        new_list.append(i)

print(f'Дублирующие элементы - {new_list}')
