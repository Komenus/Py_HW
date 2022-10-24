# Реализуйте алгоритм перемешивания списка.
from random import randint
def mix_list(list_origin):
    list = list_origin[:]
    list_len = len(list)
    for i in range(list_len):
        index_new = randint (0, list_len-1)
        temp = list[i]
        list[i] = list[index_new]
        list[index_new] = temp
    return list
list = [1,2,3,4,5,6,7,8,9]
mixed_list = mix_list(list)
print('Исходный список: ')
print(list)
print('Перемешанный список: ')
print(mixed_list)
        