# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
n = int(input('Введите число элементов списка '))
from random import randint
list1 = []
for i in range(n):
    list1.append(randint (1, 100))
print(list1)
j = len(list1) - 1
i = 0
result = 1
while i <= j:
    result = list1[i] * list1[j]
    print(f'Произведение пары чисел = {result} ')
    i+=1
    j-=1