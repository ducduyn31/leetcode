def numJewelsInStones(J: str, S: str) -> int:
    count = 0
    for s in S:
        if s in J:
            count += 1

    return count


if __name__ == '__main__':
    print(numJewelsInStones('aA', 'aAAbbbb'))
    print(numJewelsInStones('z', 'ZZ'))
