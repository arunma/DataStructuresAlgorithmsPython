from typing import Optional

from leetcode.commons.ListNode import ListNode


class MergeTwoLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        ret = ListNode()
        head = ret

        while list1 and list2:
            if list1.val < list2.val:
                ret.next = ListNode(list1.val)
                list1 = list1.next
            else:
                ret.next = ListNode(list2.val)
                list2 = list2.next
            ret = ret.next

        if list1:
            ret.next = list1
        elif list2:
            ret.next = list2

        return head.next


if __name__ == '__main__':
    init = MergeTwoLists()
