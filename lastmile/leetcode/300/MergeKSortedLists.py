import heapq
from typing import List

from ListNode import ListNode

from queue import PriorityQueue
class MergeKSortedLists:
        def mergeKLists(self, lists):
            head = curr = ListNode(0)

            pq = PriorityQueue()
            for each in lists:
                if each:
                    pq.put((each.val, each))

            while not pq.empty():
                val, node = pq.get()
                curr.next = ListNode(val)
                curr = curr.next
                node = node.next
                if node:
                    pq.put((node.val, node))

            return head.next


if __name__ == '__main__':
    init = MergeKSortedLists()
#https://leetcode.com/problems/merge-k-sorted-lists/
