import sys

from ListNode import ListNode


class RemoveDuplicatesFromSortedListII:
    # def deleteDuplicates(self, curr: ListNode) -> ListNode:
    #     dummy=ListNode(float('-inf'))
    #     dummy.next=curr
    #     prev=dummy
    #
    #     while curr and curr.next:
    #         if curr.val==curr.next.val:
    #             while curr.val==curr.next.val:
    #                 curr=curr.next
    #             curr=curr.next
    #             prev=curr
    #         else:
    #             prev.next=curr
    #             curr=curr.next
    #     return dummy.next

    def deleteDuplicates(self, curr: ListNode) -> ListNode:
        dummy=ListNode(float('-inf'))
        prev=dummy
        result=dummy

        while curr and curr.next:
            if prev.val!=curr.val and curr.val!=curr.next.val:
                result.next=curr
                result=result.next
            prev=curr
            curr=curr.next

        if prev.val!=curr.val:
            result.next=curr
            result=result.next

        result.next=None

        return dummy.next



if __name__ == '__main__':
    init = RemoveDuplicatesFromSortedListII()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    l2 = ListNode(1, ListNode(2, ListNode(2)))
    #print(init.deleteDuplicates(l1))
    print(init.deleteDuplicates(l2))
