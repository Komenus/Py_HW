# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


def subseq (n, func):
    result = []
    for i in range(1, n+1):
        result.append(round(func(i), 3))
    print(result)
    print()
    print(sum(result))
    
def main_func(n):
    return (1+ 1/n) ** n   

subseq(int(input('Введите целое число: ')), main_func )    