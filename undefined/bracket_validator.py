def is_valid(code):
    # Determine if the input code is valid
    bracket_stack = []
    top = 0

    for i in range(len(code)):
        if code[i] in ['{', '[', '(']:
            bracket_stack.insert(top, code[i])
            top += 1
            continue

        if top == 0:
            return False

        if code[i] == '}':
            if bracket_stack[top - 1] == '{':
                bracket_stack.pop()
                top -= 1
            else:
                return False
        elif code[i] == ']':
            if bracket_stack[top - 1] == '[':
                bracket_stack.pop()
                top -= 1
            else:
                return False
        elif code[i] == ')':
            if bracket_stack[top - 1] == '(':
                bracket_stack.pop()
                top -= 1
            else:
                return False

    return top == 0


if __name__ == '__main__':
    print(is_valid('([]{[]})[]{{}()}'))