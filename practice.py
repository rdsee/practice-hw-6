# info = 123, 'info1'
# print(info)
# print(type(info))
#
# nums = int(input('Enter a number: '))
# tuple1 = 1, nums, int(input('Enter a number: '))
# print(tuple1)
#
#
# import copy
#
# info = 123, 'll', 3.24
# test = copy.deepcopy(info)
# print(test)
#
# info_copy = info
# print(info_copy)
# info_list = list(info_copy)
# print(info_list)
# info_list.append('23')
# print(info_list)
# info = tuple(info_list)
# print(info)
# print(info[2:3])
# print(info[0:3:2])

# print(range(5))
# print(range(1, 5))
# print(range(1, 5, 2))
# result = range(5)
# print(result)
# print(type(result))
#
# numbers = list(range(10))
# print(numbers)
#
# numbers = list(range(3, 10))
# print(numbers)
#
# numbers = list(range(1, 10, 2))
# print(numbers)
#
# numbers = list(range(10, 0, -1))
# print(numbers)
#
# numbers = tuple(range(10, 0, -1))
# print(numbers)
#
# result = sorted(numbers)
# print(result)
# print(numbers)

# users = {
# 	4: 'key',
# 	2: 234,
# 	3: True,
#     'key': 2,
# 	False: 'pen',
# 	True: 33
# }
#
# print(users)
# print(type(users))
# print(users['key'])
# print(users[0])
# print(users[1])
# print(users[2])
# print(users[3])
# print(users[4])
# print(users[True])
# print(users[False])

# users = {
# 	"+111111":"Bob",
# 	"+222222":"Alice",
# 	"+333333":"Bob"
# }
#
# print(users)
# users['+444444'] = 'Victor'
# print(users)
# users["+111111"] = 'Tom'
# print(users)
#
# for key in users:
# 	print(key, end = ', ')
# print('\n')
#
# for keys in users.keys():
# 	print(keys, end = ', ')
# print('\n')
#
# for value in users.values():
# 	print(value, end = ', ')
#
# for key, value in users.items():
# 	print(f'key: {key}, value: {value}')

# users = {
#     "+111111": "Bob",
#     "+222222": "Alice",
#     "+333333": "Tom"
# }
#
# users2 = {
#     "+12": "Robin",
#     "+13": "Ali",
#     "+14": "Tomik"
# }
#
# # get(key) — возвращает значение по ключу; если ключ не найден, возвращает None (или default)
# print(users.get("+111111"))        # Bob
# print(users.get("+999999"))        # None — ключа нет, но ошибки не будет
# print(users.get("+999999", "N/A")) # N/A — значение по умолчанию
#
# # pop(key) — удаляет пару из словаря и возвращает значение
# removed = users.pop("+222222")
# print(removed)   # Alice
# print(users)     # Alice больше нет
#
# # copy() — создаёт поверхностную копию словаря
# users_copy = users.copy()
# users.pop("+333333")   # удаляем из оригинала
# print(users)           # Tom удалён
# print(users_copy)      # копия не изменилась — она независима
#
# # update(other) — добавляет все пары из другого словаря (или перезаписывает существующие)
# users_copy.update(users2)
# print(users_copy)      # в копии теперь и старые и новые номера
# print(users)
# # len() — количество пар в словаре
# print(len(users_copy))
# print(len(users))
#
# # clear() — удаляет все элементы словаря
# users2.clear()
# print(users2)   # {}

users = {
    1:
        {
            "name": "Petro",
            "age": 20,
            "hobbies": ["running" , "swimming"],
            "siblings": ["Kira", "Bob", "Martin"],
            "height": 1.74,
            "man": True
        },
    2:
        {
            "name": "Sofia",
            "age": 19,
            "hobbies": ["tennis" , "soccer"],
            "siblings": False,
            "height": 1.64,
            "woman": True
        },
    (3, 4):
        {
            "name": ["Oleg" , "Olga"],
            "age": [21, 24],
            "hobbies": {
                "first_person": ["football", "hockey"],
                "second_person": ["yoga", "pilates"]
            },
            "height": (1.80, 1.60),
            "sex": [
                "male",
                "female"
            ]
    }
}

print(users[2]["name"])
print(users[1]["name"])
print(users[(3, 4)]["name"][1])
print(users[(3, 4)]["hobbies"]["second_person"][0])
print(users[(3, 4)]["height"][0])
print(users[(3, 4)]["sex"][1])

