from typing import List, Union


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

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


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def reverse_list_node(l: ListNode):
        if not l.next:
            return l
        next_list = reverse_list_node(l.next)
        last_node = next_list
        while last_node.next:
            last_node = last_node.next
        l.next = None
        last_node.next = l
        return next_list

    def addTwoNodes(l1: ListNode, l2: ListNode, c: int):

        a = 0
        b = 0

        if l1 is not None:
            a = l1.val
        if l2 is not None:
            b = l2.val

        r = a + b + c

        c = 0

        if r >= 10:
            r -= 10
            c = 1

        return ListNode(r), c

    rev_l1 = reverse_list_node(l1)
    rev_l2 = reverse_list_node(l2)

    res, c = addTwoNodes(rev_l1, rev_l2, 0)

    temp = res
    A = rev_l1.next
    B = rev_l2.next

    while c is not 0 or A is not None or B is not None:

        R, c = addTwoNodes(A, B, c)

        temp.next = R
        temp = temp.next

        if A is not None:
            A = A.next

        if B is not None:
            B = B.next

    return reverse_list_node(res)


if __name__ == '__main__':
    print(addTwoNumbers(LinkedList.from_list([7, 2, 4, 3]), LinkedList.from_list([5, 6, 4])))
