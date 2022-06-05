from typing import Optional

from leetcode.commons.ListNode import ListNode


class SwapNodesInPairs:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        rethead=dummy

        return rethead


if __name__ == '__main__':
    init = SwapNodesInPairs()
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))  # 1,2,3,4
    print(init.swapPairs(l1))


prev = dummy, first = head;
while (first != null & & first.next != null) {
ListNode second = first.next, temp = second.next;
second.next = first;
first.next = temp;
prev.next = second;
prev = first;
first = temp;
}