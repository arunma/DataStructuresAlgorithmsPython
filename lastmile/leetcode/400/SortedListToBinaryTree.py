from ListNode import ListNode
from TreeNode import TreeNode


class SortedListToBinaryTree:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        prev=None
        slow=head
        fast=head

        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next

        right=slow.next
        root=TreeNode(slow.val)
        prev.next=None
        left=head

        root.left=self.sortedListToBST(left)
        root.right=self.sortedListToBST(right)

        return root





if __name__ == '__main__':
    init = SortedListToBinaryTree()
    print(init.sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))
