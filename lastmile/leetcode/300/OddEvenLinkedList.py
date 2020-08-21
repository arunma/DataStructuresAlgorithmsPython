from ListNode import ListNode


class OddEvenLinkedList:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd=head
        even=head.next
        evenHead=even

        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=evenHead
        return head




if __name__ == '__main__':
    init = OddEvenLinkedList()
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))  # 1->3->5->2->4->NULL
    print(init.oddEvenList(l2))
