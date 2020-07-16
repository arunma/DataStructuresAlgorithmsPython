class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "{}".format(self.val)


class SortList:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        l1 = self.sortList(head)  # first half
        l2 = self.sortList(slow)  # second half
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        merged = ListNode(0)
        ret = merged
        while l1 and l2:
            if l1.val < l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        merged.next = l1 or l2
        return ret.next


if __name__ == '__main__':
    init = SortList()
    l1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))  # 1,2,3,4
    l2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))  # -1->0->3->4->5
    print(init.sortList(l1))
    print(init.sortList(l2))
