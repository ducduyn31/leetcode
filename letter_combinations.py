from typing import List


def letterCombinations(digits: str) -> List[str]:
    if len(digits) == 0:
        return []

    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def letter_generator(next_letter: int, letters: List[str]) -> List[str]:
        if next_letter == len(letters) - 1:
            return phone[letters[next_letter]]

        result = []

        for k in phone[letters[next_letter]]:
            for l in letter_generator(next_letter + 1, letters):
                result.append(k + l)

        return result

    return letter_generator(0, list(digits))


if __name__ == '__main__':
    print(letterCombinations('23'))
    print(letterCombinations(''))
    print(letterCombinations('2'))
