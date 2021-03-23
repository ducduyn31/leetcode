import heapq
from collections import Counter


def frequencySort(s: str) -> str:
    words_freq = Counter(s)
    r = ''

    for char, freq in words_freq.most_common():
        r += char * freq

    return r


if __name__ == '__main__':
    print(frequencySort('tree'))
    print(frequencySort('cccaaa'))
    print(frequencySort('Aabb'))
