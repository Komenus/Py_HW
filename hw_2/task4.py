# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите число n '))
from random import randint
num = []
for i in range(n):
    num.append(randint (-n,n))
print(num)
path = 'file.txt'
file = open("file.txt", "r")
content = file.read().splitlines()
result = num[int(content[1])] * num[int(content[2])]
print(result)
file.close()