# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите число  '))
list_orig = [0, 1]
for i in range(k-1):
    temp = list_orig[i] + list_orig[i+1]
    list_orig.append(temp)
print(list_orig)
def make_negative(num):
    result = [x * -1 for x in num] 
    return result
list_new = make_negative(list_orig [:: -1])
print(list_new)
list_result = list_new.extend(list_orig)
print(list_new)