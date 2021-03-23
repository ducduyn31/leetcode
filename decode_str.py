def decodeString2(s: str) -> str:
    n = len(s)
    full_str = ['']

    def decodeRecursive(begin) -> (str, int):
        current_str = ['']
        first = begin
        while begin < n and s[begin].isalpha():
            begin += 1

        current_str.append(s[first:begin])

        if begin >= n or s[begin] == ']':
            return ''.join(current_str), begin + 1

        k = []

        while begin < n and s[begin].isdigit():
            k.append(s[begin])
            begin += 1

        k = int(''.join(k)) if k else 0

        loop_str, last_index = decodeRecursive(begin + 1)
        current_str.append(k * loop_str)

        return ''.join(current_str), last_index

    i = 0

    while i < n:
        next_str, end_index = decodeRecursive(i)
        full_str.append(next_str)
        i = end_index

    return ''.join(full_str)


def decodeString(s: str) -> str:
    begin_str, current_char, n = 0, 0, len(s)
    full_str_stack = []

    def get_next(begin: int) -> int:
        i = begin
        if s[begin].isdigit():
            while i < n and s[i].isdigit():
                i += 1
        elif s[begin].isalpha():
            while i < n and s[i].isalpha():
                i += 1
        return i

    while current_char < n:
        if s[current_char] == ']':
            the_str = []
            while full_str_stack and full_str_stack[-1] != '[':
                the_str.append(full_str_stack.pop())
            full_str_stack.pop()
            k = full_str_stack.pop()

            full_str_stack.append(int(k) * ''.join(the_str[::-1]))
            current_char += 1

        elif s[current_char] == '[':
            full_str_stack.append(s[current_char])
            current_char += 1
        else:
            end_index = get_next(current_char)
            full_str_stack.append(s[current_char:end_index])
            current_char = end_index

    return ''.join(full_str_stack)


if __name__ == '__main__':
    print(decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef'))
    print(decodeString('3[a]2[bc]'))
    print(decodeString('3[a2[c]]'))
    print(decodeString('2[abc]3[cd]ef'))
    print(decodeString('abc3[cd]xyz'))
