from typing import List


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


def insertionSortList(head: ListNode) -> ListNode:
    if not head:
        return head

    last = head
    now = head.next

    while now:
        next = now.next

        if now.val < last.val:
            last.next = next
            if now.val < head.val:
                now.next = head
                head = now
            else:
                temp = head

                while temp.next.val < now.val:
                    temp = temp.next

                temp.next, now.next = now, temp.next

        else:
            last = now
        now = next

    return head


if __name__ == '__main__':
    print(insertionSortList(LinkedList.from_list([4, 2, 1, 3])))
    print(insertionSortList(LinkedList.from_list([-1, 5, 3, 4, 0])))
