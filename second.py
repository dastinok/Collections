# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно
# в один из вариантов ниже: 1. Целое положительное число. 2. Вещественное пол или отриц число
# Строку в верхнем регистре, если в строке есть хотя бы одна заглавная буква
# Строку в верхнем регистре в остальных случаях

user_input = input('Введите данные: ')

#if isinstance(user_input, int): # Если у нас user_input типа int то
#    print(f'{user_input} - целое число')

if user_input.isdigit(): # Если у нас user_input число
    print(f'{user_input} - целое число')

#if user_input.isdecimal():
#    print(f'{user_input} - вещественное число')

elif user_input.replace('.','').replace('-','').isdigit(): # Убираем точки и тире на пустые строки
    print(f'{user_input} - вещественное число')

elif user_input == user_input.lower(): # Если user_input это строка в нижнем регистре
    print(f'{user_input}')

else:
    print(f'Заглавная буква есть, {user_input.upper()}')

    
