import heapq
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

    @staticmethod
    def from_list(nums: List[int]) -> 'ListNode':
        head = None
        current = None
        for i, n in enumerate(nums):
            if i == 0:
                head = ListNode(n)
                current = head
            else:
                next = ListNode(n)
                current.next = next
                current = next
        return head


def mergeKLists(lists: List[ListNode]) -> ListNode:
    nodes_val = []

    for l in lists:
        current = l
        while current:
            heapq.heappush(nodes_val, current.val)
            current = current.next

    first = ListNode(heapq.heappop(nodes_val)) if nodes_val else None
    current = first

    for i in range(len(nodes_val)):
        this_node = ListNode(heapq.heappop(nodes_val))
        current.next = this_node
        current = this_node

    return first


if __name__ == '__main__':
    print(mergeKLists(list(map(ListNode.from_list, [[-2, -1, -1, -1], []]))))
    print(mergeKLists(list(map(ListNode.from_list, [[1, 4, 5], [1, 3, 4], [2, 6]]))))
    print(mergeKLists(list(map(ListNode.from_list, []))))
    print(mergeKLists(list(map(ListNode.from_list, [[]]))))
