# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")
# for i in range(len(lst)):
#     for k in range(len(lst) + len(new_lst)):
#         count = 0
#         if lst[i] == new_lst[k]:
#             count = count +1
#             if count < 2:
#                 print(lst[i])
new_lst = [lst[0]]
for i in range(1, len(lst)):
    for j in range(len(new_lst)):
        if lst[i] == new_lst[j]:
            break
        elif j == len(new_lst)-1:
            new_lst.append(lst[i])
print(f"Уникальный список: {new_lst}")            