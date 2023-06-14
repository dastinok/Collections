# Создаем кортеж с разными типами. Получить из него словарь списков, где ключ -
# тип элемента, значение -  список элементов данного типа

my_tuple = (3, 4.5, True, 'Здарова', 5, False)
print(my_tuple)
my_dict = {}
for i in my_tuple:
    #new_list = []
    #my_dict.setdefault(type(i), [i])
    
    if type(i) not in my_dict:
        my_dict[type(i)] = [i]
    else:
        my_dict[type(i)].append(i)

print(my_dict)