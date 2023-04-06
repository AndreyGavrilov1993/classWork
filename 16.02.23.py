#Кортеж
# str="jklbnmvcx"
# tuple1 = tuple(str)
# print(tuple1)

#Множества
# set1 = {1, 2, 3, 4, 5} #Убирает повторные элементы
# print(set1)
# set2 = set("fghkjdftag") #Убирает повторные элементы
# print(set2)

# list1 = [1,2,7,4,8,9,4]
# set1 = set(list1)
# for i in set1:
#     print(i, end=" ")
#
# print(7 in set1)

# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,5,6,7,8,9}
# set1.union(set2)
# set1.isdisjoint(set2)
# print(set1)
# print(set2)

# import random
#
# set1 = {random.randint(10, 99) for i in range(12)}
# set2 = {random.randint(10, 99) for i in range(8)}
# set1&set2
# print(set1.isdisjoint(set2))
# set1.symmetric_difference_update(set2)
# set1.isdisjoint(set2)
# set1==set2
# set1.symmetric_difference(set2)
# print(set1&set2)
# print(set1)
# print(set2)
# print(set1|set2)
# print(set1-set2)
# print(set2-set1)
# print(set1^set2)

# countries = {"Россия", "Германия", "Австралия", "Австрия", "Армения"}
# while True:
#     print(countries)
#     v=input('1 - add, 2 - remove, 3 - search, 4 - find: ')
#     if v=='1':
#         countries.add(input("input country"))
#     elif v=='2':
#         countries.remove(input("remove country"))
#     elif v=='3':
#         s=input("input part of country: ")
#         for i in countries:
#             if i.startswith(s): print(i)
#     elif v=='4':
#         co=input("input country: ")
#         print(co in countries)
#     elif v=='0':
#         break
#     else: print("error")

# import random
# list1 = [random.randint(10,99) for i in range(20)]
# list2 = [random.randint(10,99) for j in range(20)]
# print(list1)
# print(list2)
# print(set(list1)&set(list2))

#Словари или хэш таблицы

# import random
# dict1={'помидоры':'овощи',
#        'огурцы':'овощи',
#        'апельсин':'фрукт',
#        'свинина':'мясо'}
#
# dict2 = {a:random.randint(10,20) for a in range(7)}
# print(dict1)
# print(dict1['апельсин'])
# print(dict2)
# print(dict2[4])
#
# dict3 = dict.fromkeys(['апельсин','помидор','банан'],0)
# print(dict3)

import random

dict3={i:random.randint(2000,5000) for i in {'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'}}

print(dict3.values())

for key, val in dict3.items():
    print(f'{key}:{val}')

key=input("input mounth: ")[:8:]
print(f'{key} : {dict3.get(key)}')