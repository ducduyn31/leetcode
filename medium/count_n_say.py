from collections import Counter


def countAndSay(n: int) -> str:
    if n == 1:
        return '1'

    sub = countAndSay(n -1)
    s = []
    current, count = sub[0], 0
    for c in sub:
        if c == current:
            count += 1
        else:
            s.append(f'{count}{current}')
            current, count = c, 1
    s.append(f'{count}{current}')

    return ''.join(s)


if __name__ == '__main__':
    print(countAndSay(1))
    print(countAndSay(4))
    print(countAndSay(5))
