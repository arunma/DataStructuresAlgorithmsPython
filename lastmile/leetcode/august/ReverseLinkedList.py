from AddTwoNumbers import ListNode


class ReverseLinkedList:
    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        curr=head

        while curr:
            temp = curr.next
            curr.next=prev
            prev=curr
            curr=temp

        return prev





if __name__ == '__main__':
    init = ReverseLinkedList()
    one = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(init.reverseList(one))
