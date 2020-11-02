import heapq
from typing import List

from ListNode import ListNode

from queue import PriorityQueue


class MergeKSortedLists:
    # def mergeKLists(self, lists):
    #     head = curr = ListNode(0)
    #
    #     pq = PriorityQueue()
    #     for each in lists:
    #         if each:
    #             pq.put((each.val, each))
    #
    #     while not pq.empty():
    #         val, node = pq.get()
    #         curr.next = ListNode(val)
    #         curr = curr.next
    #         node = node.next
    #         if node:
    #             pq.put((node.val, node))
    #
    #     return head.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     pq = []
    #
    #     dummy = head = ListNode(0)
    #
    #     for index, each in enumerate(lists):
    #         if each:
    #             heapq.heappush(pq, (each.val, index, each))
    #
    #     while pq:
    #         val, index, node = heapq.heappop(pq)
    #         head.next = ListNode(val)
    #         head=head.next
    #         node = node.next
    #
    #         if node:
    #             heapq.heappush(pq, (node.val, index, node))
    #
    #     return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []

        dummy = head = ListNode(0)

        for index, each in enumerate(lists):
            if each:
                heapq.heappush(pq, (each.val, each))

        while pq:
            val, node = heapq.heappop(pq)
            head.next = ListNode(val)
            head = head.next
            node = node.next

            if node:
                heapq.heappush(pq, (node.val, node))

        return dummy.next


if __name__ == '__main__':
    init = MergeKSortedLists()
    one = ListNode(1, ListNode(4, ListNode(5)))
    two = ListNode(1, ListNode(3, ListNode(4)))
    three = ListNode(2, ListNode(6))
    print(init.mergeKLists([one, two, three]))
# https://leetcode.com/problems/merge-k-sorted-lists/
