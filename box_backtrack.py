from typing import List


def fitRoom(boxV: int, roomV: int):
    return boxV <= roomV


def backtrack(states: List[int], boxes: List[int], rooms: List[int], nextBox: int):
    N = len(states) - 1

    if nextBox >= N:
        return True, states

    for i in range(-1, len(rooms))[::-1]:
        if fitRoom(boxes[nextBox], rooms[i]):
            states[nextBox] = i - 1
            rooms[i] -= boxes[nextBox]

            if backtrack(states, boxes, rooms, nextBox + 1):
                return True, states

            states[nextBox] = -1

    return False, states


if __name__ == '__main__':
    boxes = [48, 30, 42, 36, 36, 48, 42, 42, 36, 24, 30, 30, 42, 36, 36]
    rooms = [sum(boxes), 100, 100]

    print(backtrack([-1] * len(boxes), boxes, rooms, 0)[1])
