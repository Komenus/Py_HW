# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
d = [2,3,5,9,3]
result = 0
for i in range(len(d)):
    # result = 0
    if (i-1)  //2 != 0 and i != 0:
        result += d[i]
print(f'Сумма элементов на нечетных позициях {result} ')