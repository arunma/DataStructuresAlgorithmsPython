class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}, {}".format(self.val, self.next)


class AddTwoNumbers:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(0)
        node = sentinel
        carry = 0
        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            total = v1 + v2
            carry, value = divmod(total + carry, 10)
            node.next = ListNode(value)
            node = node.next

        return sentinel.next


if __name__ == '__main__':
    init = AddTwoNumbers()
    one = ListNode(2, ListNode(4, ListNode(3)))
    two = ListNode(5, ListNode(6, ListNode(4)))
    print(init.addTwoNumbers(one, two))  # 708
    one = ListNode(2, ListNode(4))
    two = ListNode(5, ListNode(6, ListNode(1)))
    print(init.addTwoNumbers(one, two))  # 702
