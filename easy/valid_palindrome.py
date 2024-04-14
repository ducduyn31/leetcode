import re


def isPalindrome(s: str) -> bool:
    s = re.sub(r'[\W_]+', '', s).lower()
    return s == s[::-1]


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
    print(isPalindrome("ab_a"))
