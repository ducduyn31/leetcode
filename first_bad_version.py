# versions = [True, True, True, True, True, False, False, False, False, False, False]
versions = [True, False]
versions = [False]


def isBadVersion(version) -> bool:
    return not versions[version - 1]


def firstBadVersion(n: int) -> int:
    left, right = 1, n
    mid = (left + right) // 2

    while left < right:
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

        mid = (left + right) // 2

    return mid


if __name__ == '__main__':
    print(firstBadVersion(len(versions)))
