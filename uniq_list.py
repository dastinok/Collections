# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список с уник элементами исходного
# 2 решения, короткое и длинное

import random

numbers = []

for i in range(21):
    numbers.append(random.randint(0,10))

print(numbers)

numbers = list(set(numbers)) #

print(numbers)


new_numbers = []
for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)

print(new_numbers)


