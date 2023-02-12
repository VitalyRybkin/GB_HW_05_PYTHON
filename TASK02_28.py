"""
Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

2 2
4
"""

while True:
    A = input('Введите число А или "Q": ')
    if A == 'Q':
        exit('Завершено пользователем!')
    A = int(A)
    B = input('Введите число B или "Q": ')
    if B == 'Q':
        exit('Завершено пользователем!')
    B = int(B)

    res = A
    step = 1

    def num_power(step, result):
        if B == step:
            return result + 1
        else:
            return num_power(step + 1, result + 1)

    print(num_power(step, res))