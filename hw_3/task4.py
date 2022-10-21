# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите десятичное число  '))
def bin(num):
    list1 = []
    while num not in [0, 1]:
        temp = num % 2
        num = num // 2 
        list1.append(temp)
    list1.append(num)    
    bin_num = ''.join(map(str, list1[:: -1]))
    return bin_num
print(bin(n))
