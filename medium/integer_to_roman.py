from math import log

def intToRoman(num: int) -> str:
    dictionary = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

    result = []

    # while num > 0:

    return ''.join(result)


if __name__ == '__main__':
    # print(intToRoman(3))
    # print(intToRoman(4))
    # print(intToRoman(9))
    # print(intToRoman(58))
    # print(intToRoman(1994))
    d = {'I': [], 'V': [], 'X': [], 'L': [], 'C': [], 'D': [], 'M': []}
    l = [[], [], [], [], [], [], []]
    for i in range(1, 100, 1):
        b = int(log(i, 5))
        a = int((log(i, 5) - b) / log(2, 5))
        l[a + b].append(i)

    print(l)
