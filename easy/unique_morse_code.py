from typing import List


def uniqueMorseRepresentations(words: List[str]) -> int:
    alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    ans = set()

    for word in words:
        ans.add(''.join([alphabet[ord(c) - ord('a')] for c in word]))

    return len(ans)


if __name__ == '__main__':
    print(uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg']))
