from typing import Optional

from lastmile.leetcode.commons.ListNode import ListNode


class DeleteTheMiddleNodeOfLinkedList:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(0)
        sent.next = head
        slow = sent
        fast = sent

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next=slow.next.next
        return sent.next


if __name__ == "__main__":
    init = DeleteTheMiddleNodeOfLinkedList()
    ll = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    init.deleteMiddle(ll)  # [1,3,4,1,2,6]
    print(ll)
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    init.deleteMiddle(ll)  # [1,2,4]
    ll = ListNode(2, ListNode(1))
    init.deleteMiddle(ll)  # [2]
