from typing import List


def intervalIntersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    result = []

    A_pointer = 0
    B_pointer = 0

    while A_pointer < len(A) and B_pointer < len(B):
        current_intersect = [-1, -1]

        if A[A_pointer][0] > B[B_pointer][1]:
            B_pointer += 1
            continue
        elif B[B_pointer][0] > A[A_pointer][1]:
            A_pointer += 1
            continue

        if A[A_pointer][0] < B[B_pointer][0]:
            current_intersect[0] = B[B_pointer][0]
            if B[B_pointer][1] >= A[A_pointer][1]:
                current_intersect[1] = A[A_pointer][1]
                A_pointer += 1
            else:
                current_intersect[1] = B[B_pointer][1]
                B_pointer += 1

            result.append(current_intersect)
        else:
            current_intersect[0] = A[A_pointer][0]
            if A[A_pointer][1] >= B[B_pointer][1]:
                current_intersect[1] = B[B_pointer][1]
                B_pointer += 1
            else:
                current_intersect[1] = A[A_pointer][1]
                A_pointer += 1

            result.append(current_intersect)

    return result


if __name__ == '__main__':
    print(intervalIntersection([[4, 6], [7, 8], [10, 17]], [[5, 10]]))
    print(intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]))
