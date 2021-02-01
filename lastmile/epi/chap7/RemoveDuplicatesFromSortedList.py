from ListNode import ListNode


class RemoveDuplicatesFromSortedList:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr=head
        while curr and curr.next:
            if curr.val==curr.next.val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return head

if __name__ == '__main__':
    init = RemoveDuplicatesFromSortedList()
    one = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    print(init.deleteDuplicates(one))
