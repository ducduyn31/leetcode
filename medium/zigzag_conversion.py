def convert(s: str, numRows: int) -> str:
    l = len(s)
    result = []

    for row in range(numRows):
        cursor = row

        while cursor < l:
            result.append(s[cursor])

            if row != numRows - 1 and (cursor - row) % (2 * numRows - 2) == 0:
                cursor += 2 * (numRows - row - 1)
            else:
                if row != 0:
                    cursor += 2 * row
                else:
                    cursor += 1

    return ''.join(result)


if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 3))
    print(convert('PAYPALISHIRING', 4))
    print(convert('A', 1))
