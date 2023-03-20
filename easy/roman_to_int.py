def romanToInt(s: str) -> int:
    look_up = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0

    for i, c in enumerate(s):
        sum += look_up[c]
        if i > 0 and look_up[c] > look_up[s[i - 1]]:
            sum -= 2 * look_up[s[i-1]]

    return sum


if __name__ == '__main__':
    print(romanToInt('III'))
    print(romanToInt('IV'))
    print(romanToInt('IX'))
    print(romanToInt('LVIII'))
    print(romanToInt('MCMXCIV'))