from typing import List


def shortestToChar(S: str, C: str) -> List[int]:
    C_pos = []
    result = []
    last, next = -1, -1

    for pos, char in enumerate(S):
        if char == C:
            C_pos.append(pos)

    current_target = 0
    next = C_pos[current_target]

    for pos, char in enumerate(S):
        if last == -1:
            result.append(next - pos)
        elif next == -1:
            result.append(pos - last)
        else:
            result.append(min(next - pos, pos - last))

        if char == C:
            current_target += 1
            if current_target == len(C_pos):
                next = - 1
                last = C_pos[-1]
            else:
                last = next
                next = C_pos[current_target]

    return result


if __name__ == '__main__':
    print(shortestToChar('loveleetcode', 'e'))
