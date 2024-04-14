def maxPower(s: str) -> int:
    power = [1]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            power.append(power[i - 1] + 1)
        else:
            power.append(1)

    return max(power)


if __name__ == '__main__':
    print(maxPower('leetcode'))
    print(maxPower('abbcccddddeeeeedcba'))
    print(maxPower('triplepillooooow'))
    print(maxPower('hooraaaaaaaaaaay'))
    print(maxPower('tourist'))
