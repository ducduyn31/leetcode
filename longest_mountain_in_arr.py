from typing import List


# class MountainPart:
#     BEGIN = 'BEGIN'
#     TOP = 'TOP'
#     END = 'END'
#
#
# look_for = MountainPart.BEGIN
# current_mountain_len = 0
# max_mountain_len = 0
#
# step = 1
#
# while step < len(A) - 1:
#     if look_for == MountainPart.BEGIN and not A[step] > A[step - 1]:
#         current_mountain_len = 0
#     elif (look_for == MountainPart.TOP or look_for == MountainPart.BEGIN) and A[step - 1] < A[step] > A[step + 1]:
#         look_for = MountainPart.END
#         current_mountain_len += 1
#     elif look_for == MountainPart.BEGIN and A[step] > A[step - 1]:
#         look_for = MountainPart.TOP
#         current_mountain_len += 1
#     elif look_for == MountainPart.TOP and A[step] > A[step - 1]:
#         current_mountain_len += 1
#     elif look_for == MountainPart.END and A[step - 1] > A[step]:
#         current_mountain_len += 1
#     elif look_for == MountainPart.END and not A[step - 1] > A[step]:
#         look_for = MountainPart.BEGIN
#         step -= 1
#         max_mountain_len = max(max_mountain_len, current_mountain_len + 1)
#         continue
#
#     step += 1
#
# if look_for == MountainPart.END:
#     if A[-1] < A[-2]:
#         current_mountain_len += 1
#     max_mountain_len = max(max_mountain_len, current_mountain_len + 1)
#
# return max_mountain_len

def longestMountain(A: List[int]) -> int:
    if len(A) < 3:
        return 0

    step = 1
    max_len = 0

    while step < len(A):

        begin = step - 1

        if A[step - 1] < A[step]:

            while step < len(A) and A[step - 1] < A[step]:
                step += 1

            if step >= len(A) or not A[step - 1] > A[step] :
                continue

            while step < len(A) and A[step - 1] > A[step]:
                step += 1

            max_len = max(max_len, step - begin)
            continue

        step += 1

    return max_len



if __name__ == '__main__':
    # print(longestMountain([0, 1, 0, 1, 0, 1]))
    # print(longestMountain(
    #     [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1,
    #      0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0,
    #      0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1]))
    print(longestMountain([875, 884, 239, 731, 723, 685]))
    print(longestMountain([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(longestMountain([0, 1, 0]))
    print(longestMountain([2, 1, 4, 7, 3, 2, 5]))
    print(longestMountain([2, 2, 2]))
