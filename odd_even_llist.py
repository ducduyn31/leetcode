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


def oddEvenList(head: ListNode) -> ListNode:
    if not head:
        return head

    odd = last_odd = head
    current = even = last_even = head.next
    isOdd = True

    while current:
        if isOdd:
            last_odd.next = current = current.next
            if last_odd.next:
                last_odd = last_odd.next
            isOdd = False
        elif last_even:
            last_even.next = current = current.next
            last_even = last_even.next
            isOdd = True

    last_odd.next = even

    return odd


if __name__ == '__main__':
    print(oddEvenList(LinkedList.from_list([])))
    print(oddEvenList(LinkedList.from_list([1, 2, 3, 4, 5, 6, 7, 8])))
    print(oddEvenList(LinkedList.from_list([1])))
    print(oddEvenList(LinkedList.from_list([1, 2, 3, 4, 5])))
    print(oddEvenList(LinkedList.from_list([2, 1, 3, 5, 6, 4, 7])))
