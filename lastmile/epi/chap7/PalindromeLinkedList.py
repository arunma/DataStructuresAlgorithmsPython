from ListNode import ListNode


class PalindromeLinkedList:
    def isPalindrome(self, head: ListNode) -> bool:
        slow=head
        fast=head

        #Find mid
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #Reverse LL
        revHead=None
        while slow:
            next=slow.next
            slow.next=revHead
            revHead=slow
            slow=next

        #Check palin
        while revHead:
            if head.val!=revHead.val:
                return False
            head=head.next
            revHead=revHead.next

        return True



if __name__ == '__main__':
    init = PalindromeLinkedList()
    #l1 = ListNode(1, ListNode(2,ListNode(1)))
    l2 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(1))))
    #print(init.isPalindrome(l1))
    print(init.isPalindrome(l2))
    print(init.isPalindrome(l3))
