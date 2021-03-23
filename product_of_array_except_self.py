from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    output = [1]

    for i in range(1, len(nums), 1):
        output.append(output[i - 1] * nums[i - 1])

    product_from_last = 1

    for i in range(len(nums) - 1, -1, -1):
        output[i] = product_from_last * output[i]
        product_from_last *= nums[i]

    return output


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([2, 3]))
