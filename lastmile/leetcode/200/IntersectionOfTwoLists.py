class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}".format(self.val)


def get_length(head):
    count=0
    while head:
        count=count+1
        head=head.next
    return count



class IntersectionOfTwoLists:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        lenA=get_length(headA)
        lenB=get_length(headB)

        while lenA>lenB:
            lenA=lenA-1
            headA=headA.next

        while lenB>lenA:
            headB=headB.next
            lenB=lenB-1

        while headA!=headB:
            headA=headA.next
            headB=headB.next

        return headA



if __name__ == '__main__':
    init = IntersectionOfTwoLists()
    c=ListNode(8, ListNode(4, ListNode(5)))
    a = ListNode(4, ListNode(1, c))
    b = ListNode(5, ListNode(0, ListNode(1, c)))
    print(init.getIntersectionNode(a, b)) #8
