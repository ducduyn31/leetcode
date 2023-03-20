def smallestRepunitDivByK(K: int) -> int:
    if K % 10 not in {1, 3, 7, 9}:
        return -1

    mod_set = set()
    mod = 0

    for i in range(1, K + 1):
        mod = (10 * mod + 1) % K
        if mod == 0:
            return i
        if mod in mod_set:
            return -1
        mod_set.add(mod)




if __name__ == '__main__':
    print(smallestRepunitDivByK(49993))
    print(smallestRepunitDivByK(7))
    print(smallestRepunitDivByK(1))
    print(smallestRepunitDivByK(2))
    print(smallestRepunitDivByK(3))
