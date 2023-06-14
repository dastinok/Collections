# Создать список с повторением элементов
# Удалите из него все элементы, которые встречаются дважды

my_list = [1, 2, 3, 5, 5, 5, 5, 3, 4, 0, 0, 6, 9, 1]

#for i in my_list:
#    if my_list.count(i) == 2:
#        my_list.remove(i)
#        my_list.remove(i)
#print(my_list)
# for для перебора

i = 0
while i < len(my_list):
    if my_list.count(i) == 2:
        my_list.remove(i)
        my_list.remove(i)

    else:
        i += 1
print(my_list)

