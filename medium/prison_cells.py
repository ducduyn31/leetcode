from typing import List


def prisonAfterNDays(cells: List[int], N: int) -> List[int]:
    def next_day_state(today_state: List[int]) -> List[int]:
        next_day = [0] * len(today_state)

        for cell in range(1, len(cells) - 1):
            if cells[cell - 1] == cells[cell + 1]:
                next_day[cell] = 1

        return next_day

    n = (N - 1) % 14 + 1

    next_day = []
    for day in range(n):
        next_day = next_day_state(cells)
        cells = next_day

    return next_day


if __name__ == '__main__':
    print(prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
    print(prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000))
