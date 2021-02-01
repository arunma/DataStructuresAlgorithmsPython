from ListNode import ListNode


class RemoveNthNodeFromEndList:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast=head
        for _ in range(n):
            fast=fast.next

        if not fast:
            return head.next #IMPORTANT and Easy to miss for cases like [1]-1, [1,2]-2

        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next
        return head



if __name__ == '__main__':
    init = RemoveNthNodeFromEndList()
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(init.removeNthFromEnd(l2, 2))
