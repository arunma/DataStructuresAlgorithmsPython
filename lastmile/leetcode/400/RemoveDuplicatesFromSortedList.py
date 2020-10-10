from AddTwoNumbers import ListNode


class RemoveDuplicatesFromSortedList:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        if not head.next:
            return head

        curr = head.next
        prev = head

        while curr:
            if prev.val == curr.val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return head


if __name__ == '__main__':
    init = RemoveDuplicatesFromSortedList()
