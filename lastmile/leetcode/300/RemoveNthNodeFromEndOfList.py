from SortList import ListNode


class RemoveNthNodeFromEndOfList:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next=head

        slow = head
        size = 0
        while slow:
            size += 1
            slow = slow.next

        rem_idx = size - n
        prev=dummy
        while rem_idx:
            prev=head
            head=head.next
            rem_idx-=1

        prev.next=head.next
        return dummy.next


if __name__ == '__main__':
    init = RemoveNthNodeFromEndOfList()
    one = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(init.removeNthFromEnd(one, 2))
    two = ListNode(1)
    print(init.removeNthFromEnd(two, 1))
