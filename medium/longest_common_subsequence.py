def longestCommonSubsequence(text1: str, text2: str) -> int:
    table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for j in range(len(text2)):
        for i in range(len(text1)):
            if text1[i] == text2[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])

    return table[len(text1)][len(text2)]


if __name__ == '__main__':
    print(longestCommonSubsequence('abcde', 'ace'))
    print(longestCommonSubsequence('abc', 'abc'))
    print(longestCommonSubsequence('abc', 'def'))
