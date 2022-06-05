from typing import Optional

from leetcode.commons.ListNode import ListNode


class LinkedListHasCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    init = LinkedListHasCycle()
