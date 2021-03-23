from typing import List


class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x

    def get_chain_val(self):
        if self.next is None:
            return str(self.val)

        return str(self.val) + ' - > ' + self.next.get_chain_val()

    def print(self):
        print(self.get_chain_val())

    def __str__(self):
        return self.get_chain_val()


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


def swapPairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    last = None
    current, nxt = head, head.next
    ret = nxt

    while nxt:
        current.next, nxt.next = nxt.next, current
        if last:
            last.next = nxt

        last = current
        current, nxt = current.next, None if not current.next else current.next.next

    return ret


if __name__ == '__main__':
    print(swapPairs(LinkedList.from_list([1, 2, 3, 4])))
    print(swapPairs(LinkedList.from_list([])))
    print(swapPairs(LinkedList.from_list([1])))
