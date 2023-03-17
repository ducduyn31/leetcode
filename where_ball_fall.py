from typing import List


def findBall(grid: List[List[int]]) -> List[int]:
    balls = list(range(len(grid[0])))

    def move_ball(level: int, col: int, ball_id: int, next_location: List[int]):
        # If ball is at edge and sliding to edge
        if col == 0 and grid[level][col] == -1:
            return
        if col == len(grid[0]) - 1 and grid[level][col] == 1:
            return

        # If V shape found
        if grid[level][col] == 1 and grid[level][col + 1] == -1:
            return
        if grid[level][col] == -1 and grid[level][col - 1] == 1:
            return

        # Slide ball
        if grid[level][col] == 1:
            next_location[ball_id] = col + 1
        else:
            next_location[ball_id] = col - 1

    for level in range(len(grid)):
        next_level = [-1 for _ in balls]
        for ball_id, loc in enumerate(balls):
            if loc == -1:
                continue
            move_ball(level, loc, ball_id, next_level)
        balls = next_level

    return balls


if __name__ == '__main__':
    assert findBall([
        [1, 1, 1, -1, -1],  # [1, 2, -1, -1, 3]
        [1, 1, 1, -1, -1],  # [-1, -1, -1, -1, -1]
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1]]) == [1, -1, -1, -1, -1]
    assert findBall([[-1]]) == [-1]
    assert findBall([
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1],
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1]]) == [0, 1, 2, 3, 4, -1]
