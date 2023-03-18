from typing import List


def maxSubarraySumCircular(A: List[int]) -> int:
    current_max = total_max = A[0]
    accumulate_sum = [A[0]]
    begin_to_n = [0]

    for i in range(1, len(A)):
        accumulate_sum.append(accumulate_sum[i - 1] + A[i])
        begin_to_n.append(max(accumulate_sum[i - 1], begin_to_n[i - 1]))

    for i in range(1, len(A)):
        current_max = max(A[i], current_max + A[i])

        if current_max > total_max:
            total_max = current_max

    for i in range(len(A) - 1):
        total_max = max(accumulate_sum[-1] - accumulate_sum[i] + begin_to_n[i], total_max)

    return total_max


if __name__ == '__main__':
    print(maxSubarraySumCircular([2, -2, 3, -1]))
    print(maxSubarraySumCircular([1, -2, 3, -2]))
    print(maxSubarraySumCircular([5, -3, 5]))
    print(maxSubarraySumCircular([3, -1, 2, -1]))
    print(maxSubarraySumCircular([3, -2, 2, -3]))
    print(maxSubarraySumCircular([-2, -3, -1]))
