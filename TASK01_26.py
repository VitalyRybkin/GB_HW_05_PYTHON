"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8

"""
while True:
    A = input('Введите число А или "Q": ')
    if A == 'Q':
        exit('Завершено пользователем!')
    A = int(A)
    B = input('Введите степень или "Q": ')
    if B == 'Q':
        exit('Завершено пользователем!')
    B = int(B)
    res = A

    def num_power(power, result):
        if power == 1:
            return result
        else:
            result = result * A
            return num_power(power - 1, result)

    print(num_power(B, res))

