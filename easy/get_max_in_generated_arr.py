def getMaximumGenerated(n: int) -> int:
    nums = [0, 1]

    if n <= 1:
        return nums[n]

    for i in range(2, n + 1):
        if i % 2 == 0:
            nums.append(nums[i // 2])
        else:
            nums.append(nums[i // 2] + nums[i // 2 + 1])

    return max(nums)


if __name__ == '__main__':
    for i in range(100):
        print(getMaximumGenerated(i))
    # print(getMaximumGenerated(2))
    # print(getMaximumGenerated(3))
