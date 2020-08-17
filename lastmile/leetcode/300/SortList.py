from AddTwoNumbers import ListNode


class SortList:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow=head
        fast=head
        prev=None

        while fast and fast.next:
            prev=slow
            slow = slow.next
            fast=fast.next.next

        prev.next=None #Disconnect first and second part

        left=self.sortList(head)
        right=self.sortList(slow)
        return self.merge(left, right)

    def merge(self, left, right):
        merged=ListNode()
        rethead=merged
        while left and right:
            if left.val<right.val:
                merged.next=ListNode(left.val)
                left=left.next
            else:
                merged.next = ListNode(right.val)
                right=right.next
            merged=merged.next

        merged.next=left or right
        return rethead.next


if __name__ == '__main__':
    init = SortList()
    l1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))  # 1,2,3,4
    l2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))  # -1->0->3->4->5
    print(init.sortList(l1))
    print(init.sortList(l2))