def calculate(s: str) -> int:
    s = f"{s.replace(' ', '')} "
    current_num = 0
    operator = '+'
    S = [0]

    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
            continue
        elif operator == '+':
            S.append(current_num)
        elif operator == '-':
            S.append(-current_num)
        elif operator == '*':
            S[-1] = S[-1] * current_num
        elif operator == '/':
            S[-1] = int(S[-1] / current_num)

        operator = c
        current_num = 0

    return sum(S)


if __name__ == '__main__':
    print(calculate('1*2-3/4+5*6-7*8+9/10'))
    print(calculate('0/1'))
    print(calculate('14-3/2'))
    print(calculate('2*3+4'))
    print(calculate('3+2*2'))
    print(calculate(" 3/2 "))
    print(calculate(" 3+5 / 2 "))
