from ListNode import ListNode

class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result=dummy=ListNode(0)
        carry=0

        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next

            carry,value = divmod(carry, 10)
            result.next=ListNode(value)
            result=result.next
        return dummy.next

if __name__ == '__main__':
    init = AddTwoNumbers()
    one = ListNode(2, ListNode(4, ListNode(3)))
    two = ListNode(5, ListNode(6, ListNode(4)))
    print(init.addTwoNumbers(one, two))  # 708
    one = ListNode(2, ListNode(4))
    two = ListNode(5, ListNode(6, ListNode(1)))
    print(init.addTwoNumbers(one, two))   # 702
    one = ListNode(5)
    two = ListNode(5)
    print(init.addTwoNumbers(one, two))  #
