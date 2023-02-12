import settings as s

oper = ['+', '-', '*', '/']

def get_num2(exp):
    s.end_idx += 1
    while s.end_idx <= len(exp) - 1 and exp[s.end_idx] not in oper:
        s.num2 += exp[s.end_idx]
        s.end_idx += 1

    if s.num2.isdigit():
        s.num2 = int(s.num2)
    else:
        s.num2 = float(s.num2)


def get_num1(exp):
    if s.start_idx > 0:
        s.start_idx -= 1
    while s.start_idx >= 0 and exp[s.start_idx] not in oper:
        s.num1 += exp[s.start_idx]
        s.start_idx -= 1
    if s.start_idx < 0:
        s.start_idx = 0
    else:
        s.start_idx += 1

    if s.num1.isdigit():
        s.num1 = int(s.num1)
    else:
        s.num1 = float(s.num1)