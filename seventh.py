# Пользователь вводит строку текста подсчитайте сколько раз
# встречается каждая буква в строке без использования метода
# count и c ним. Результат сохр в словаре где ключ - символ,
# а значение - частота встречи символа в строке

text = 'Пользователь вводит строку текста подсчитайте сколько раз'

new_text = text.replace(' ','').lower()
print(new_text)
my_dict = {}

for i in set(new_text):
    my_dict[i] = new_text.count(i)
print(my_dict)

my_dict_2 = {}
for i in new_text:
    if i not in my_dict_2.keys():
        my_dict_2[i] = 1
    else:
        my_dict_2[i] += 1
print(my_dict_2)

my_dict_3 = {}
for i in text:
    my_dict_3[i] = my_dict_3.get(i, 0) + 1
print(my_dict_3)