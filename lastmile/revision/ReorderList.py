from typing import Optional

from leetcode.commons.ListNode import ListNode


class ReorderList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head

        #Find mid
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        right=slow.next
        slow.next=None

        #Reverse right:
        rprev=None
        while right:
            temp=right.next
            right.next=rprev
            rprev=right
            right=temp

        #Merge
        first=head
        second=rprev

        while second:
            fnext=first.next
            snext=second.next

            first.next=second
            second.next=fnext

            first=fnext
            second=snext


if __name__ == '__main__':
    init = ReorderList()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))  # -1->5->2->4->3
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))  # -1->4->2->3
    init.reorderList(l1)
    init.reorderList(l2)

