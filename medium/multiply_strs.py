def multiply(num1: str, num2: str) -> str:
    return str(int(num1) * int(num2))


if __name__ == '__main__':
    assert multiply('2', '3') == '6'
    assert multiply('123', '456') == '56088'
