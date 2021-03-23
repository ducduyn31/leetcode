from collections import Counter


def minDeletions(s: str) -> int:
    count = Counter(s)
    values = set()
    r = 0
    for _, n in count.most_common():
        if n not in values:
            values.add(n)
        else:
            while n in values and n > 0:
                n -= 1
                r += 1
            values.add(n)

    return r


if __name__ == '__main__':
    print(minDeletions('aab'))
    print(minDeletions('aaabbbcc'))
    print(minDeletions('ceabaacb'))
    print(minDeletions('bbcebab'))
