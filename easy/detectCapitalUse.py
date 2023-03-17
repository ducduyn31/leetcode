def detectCapitalUser(word: str) -> bool:
    isAllLow = word[0].islower()
    for c in range(1, len(word)):
        if isAllLow and word[c].isupper():
            return False

        if c == 1 and word[1].islower():
            isAllLow = True

        if not isAllLow and word[c].islower():
            return False
    return True


if __name__ == '__main__':
   print(detectCapitalUser('USA'))
   print(detectCapitalUser('leetcode'))
   print(detectCapitalUser('Leetcode'))
   print(detectCapitalUser('FlaG'))