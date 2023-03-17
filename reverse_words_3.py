def reverseWords(s: str) -> str:
    return ' '.join([token[::-1] for token in s.split(sep=' ')])


if __name__ == '__main__':
    assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverseWords("God Ding") == "doG gniD"
