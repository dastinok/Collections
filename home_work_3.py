# Создайте словарь со списком вещей в качестве ключа и их масса в качестве значения
# Определите какие вещи влезут в рюкзак передав его макс грузоподъемность
import itertools

load_capacity_backpack = input('Введите максимальную грузоподъемность рюкзака: ')


backpack = {'raincoat': 3, 'food': 5, 'hygiene': 2, 'tent': 8, 'flask': 2, 'first_aid_kit': 5,
            'extra_shoes': 3, 'clothes': 6, 'sleep_bag': 4}

print(type(backpack))

backpack_values = sum(backpack.values())
print(f'{backpack_values} кг весят вещи')
print(backpack.values())
print(type(backpack_values))

if load_capacity_backpack.isdigit() and int(load_capacity_backpack) > backpack_values:
    print(f'{int(load_capacity_backpack) - backpack_values} кг свободно. Все вместилось')

elif load_capacity_backpack.isdigit() and int(load_capacity_backpack) < backpack_values:
    print('Рюкзак переполнен. Избавьтесь от вещей')
    print(backpack_values)
    print(type(backpack_values))
    value_list = list(backpack.values())
    l1 = [[key, value] for key, value in backpack.items()]
    print(l1)
    print(type(l1))

    print(value_list)
    result = [seq for i in range(len(value_list), 0, -1) for seq in itertools.combinations(value_list, i)
              if sum(seq) == int(load_capacity_backpack)]

    print(result)
    print(type(result))

    # Тут уже не знаю как заменить числа на ключи из словаря??






