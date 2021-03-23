from typing import List


class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = dict()

    for s in strs:
        key = hashabledict([(c, s.count(c)) for c in s])

        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)

    return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    answer = groupAnagrams(strs)

    answer.sort(key=lambda x: sorted(x[0]))

    a = [hashabledict([(c, s.count(c)) for c in s]) for s in strs]

    print(a[0] == a[1])

    print(answer)
