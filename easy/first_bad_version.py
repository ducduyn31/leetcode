current_bad_version = -1


def isBadVersion(version) -> bool:
    return version == current_bad_version


def firstBadVersion(n: int) -> int:
    left = 1

    while left < n:
        mid = (left + n) // 2

        if isBadVersion(mid):
            n = mid
        else:
            left = mid + 1

    return n


def run_bad_simulator(n: int, bad: int):
    global current_bad_version
    current_bad_version = bad
    assert firstBadVersion(n) == bad


if __name__ == '__main__':
    run_bad_simulator(5, 4)
    run_bad_simulator(1, 1)
