from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, nums: List[int]):
        self.first = self.from_list(nums)

    @staticmethod
    def from_list(nums: List[int]) -> ListNode:
        first = ListNode(nums[0])
        current = first
        n = len(nums)

        for _ in range(n - 1):
            current.next = ListNode(nums[1])
            nums.pop(0)
            current = current.next

        return first

    def __str__(self):
        l = []

        current = self.first

        while current:
            l.append(current.val)
            current = current.next

        return str(l)


def getDecimalValue(head: ListNode) -> int:
    sum = 0

    current = head
    while current:
        sum = sum * 2 + current.val
        current = current.next

    return sum


if __name__ == '__main__':
    print(getDecimalValue(LinkedList.from_list([1, 0, 1])))
    print(getDecimalValue(LinkedList.from_list([0])))
    print(getDecimalValue(LinkedList.from_list([1])))
    print(getDecimalValue(LinkedList.from_list([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])))
    print(getDecimalValue(LinkedList.from_list([0, 0])))
