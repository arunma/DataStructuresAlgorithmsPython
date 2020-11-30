from ListNode import ListNode


class MergeInBetweenLinkedLists:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        front=None
        head=list1

        while head.val!=a:
            front=head
            head=head.next

        back=None
        head=list1
        while head.val!=b:
            back=head
            head=head.next
        back=head.next

        front.next=list2

        l2tail=None
        l2head=list2
        while l2head:
            l2tail=l2head
            l2head=l2head.next

        l2tail.next=back

        return list1




if __name__ == '__main__':
    init = MergeInBetweenLinkedLists()
    l1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    l2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    print(init.mergeInBetween(l1, 3, 4, l2))
