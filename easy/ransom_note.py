def canConstruct(ransomNote: str, magazine: str) -> bool:
    for c in ransomNote:
        if not c in magazine:
            return False
        magazine = magazine.replace(c, "", 1)
    return True


if __name__ == '__main__':
    print(canConstruct('a', 'b'))
    print(canConstruct('aa', 'ab'))
    print(canConstruct('aa', 'aab'))
