import math


def climbStairs(n: int) -> int:
    phi = ( 1 + math.sqrt(5)) / 2
    return round((phi ** (n + 1) - (1 - phi)**(n+1))/ math.sqrt(5))


if __name__ == '__main__':
    print(climbStairs(2))
    print(climbStairs(3))
