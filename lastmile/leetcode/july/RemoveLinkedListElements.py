from AddTwoNumbers import ListNode


class RemoveLinkedListElements:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sent = ListNode(0)
        sent.next = head
        prev, curr = sent, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sent.next


if __name__ == '__main__':
    init = RemoveLinkedListElements()
    one = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    print(init.removeElements(one, 6))
    two = ListNode(1)
    print(init.removeElements(two, 6))
    three = None
    print(init.removeElements(three, 6))
    four = ListNode(6)
    print(init.removeElements(four, 6))
