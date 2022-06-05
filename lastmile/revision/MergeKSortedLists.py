from typing import Optional, List

from leetcode.commons.ListNode import ListNode
import heapq


class MergeKSortedLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]

        for index, each in enumerate(lists):
            if each:
                heapq.heappush(pq, (each.val, index, each))

        dummy=ret=ListNode(0)

        while pq:
            value, index, lst = heapq.heappop(pq)
            ret.next=ListNode(value)
            ret=ret.next
            lst=lst.next

            if lst:
                heapq.heappush(pq, (lst.val, index, lst))

        return dummy.next






if __name__ == '__main__':
    init = MergeKSortedLists()
    one = ListNode(1, ListNode(4, ListNode(5)))
    two = ListNode(1, ListNode(3, ListNode(4)))
    three = ListNode(2, ListNode(6))
    print(init.mergeKLists([one, two, three])) #1->1->2->3->4->4->5->6
