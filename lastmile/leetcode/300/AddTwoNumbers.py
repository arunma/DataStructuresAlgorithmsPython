class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}, {}".format(self.val, self.next)


class AddTwoNumbers:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     sent = ret = ListNode()
    #     carry = 0
    #     while l1 or l2 or carry:
    #         val1 = 0
    #         val2 = 0
    #         if l1:
    #             val1 = l1.val
    #             l1 = l1.next
    #         if l2:
    #             val2 = l2.val
    #             l2 = l2.next
    #         tot = val1 + val2 + carry
    #         carry, value = divmod(tot, 10)
    #         ret.next = ListNode(value)
    #         ret = ret.next
    #     return sent.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sent = ret = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry+= l1.val
                l1 = l1.next
            if l2:
                carry+= l2.val
                l2 = l2.next
            carry, value = divmod(carry, 10)
            ret.next = ListNode(value)
            ret = ret.next
        return sent.next


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
