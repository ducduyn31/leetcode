from typing import List


def fizzBuzz(n: int) -> List[str]:
    ans = list(range(1, n + 1))
    fizz, buzz = 3, 5

    for i in range(n):
        msg = []
        if (i + 1) % fizz == 0:
            msg.append('Fizz')
        if (i + 1) % buzz == 0:
            msg.append('Buzz')

        ans[i] = ''.join(msg) if msg else str(ans[i])

    return ans


if __name__ == '__main__':
    print(fizzBuzz(15))
