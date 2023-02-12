"""
Урок 5. Рекурсия и алгоритмы
задача калькулятор необязательная.
Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
Например,

"""

"""
1+9/3*7-4 = 18
1.2+23*19/14 = 32.48
13*25*29/34+27/18 = 277.75
13+2/4*25*29/34+27/3*18 = 185.62
"""
import set_nums as sn
import settings as s

def main():
    while True:
        s.exp = []
        n = input('Введите выражение или "Q": ')
        if n == 'Q':
            exit()
        n = n.replace(',', '.')
        n_list = list(n)
        str_to_write = ''
        for i in range(len(n_list)):
            if n_list[i] == ' ':
                continue
            if n_list[i].isdigit() or n_list[i] == '.':
                str_to_write += n_list[i]
                if i == len(n_list) - 1:
                    s.exp.append(str_to_write)
            else:
                s.exp.append(str_to_write)
                s.exp.append(n_list[i])
                str_to_write = ''
        #print(s.exp)
        print('Результат:', calc(s.exp))


def calc(exp_list):
    s.num1 = ''
    s.num2 = ''
    s.start_idx = 0
    s.end_idx = 0

    operator = {
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            }

    if len(exp_list) == 1:
        return s.exp[0]
    else:
        for key,_ in operator.items():
            op = key
            if op in exp_list:
                s.end_idx = s.start_idx = exp_list.index(op)
                sn.get_num1(exp_list)
                sn.get_num2(exp_list)
                del exp_list[s.start_idx : s.end_idx]
                res = operator[op](s.num1, s.num2)
                if res % 10 != 0:
                    res = round(res, 2)
                exp_list.insert(s.start_idx, str(res))
                return calc(exp_list)

main()