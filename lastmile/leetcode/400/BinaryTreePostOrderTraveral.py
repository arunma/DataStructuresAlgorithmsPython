import collections
from typing import List

from TreeNode import TreeNode


class BinaryTreePostOrderTraveral:
#https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []
        result = collections.deque()

        while node or stack:
            if node:
                result.appendleft(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return list(result)



if __name__ == '__main__':
    init = BinaryTreePostOrderTraveral()
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.right = TreeNode(6)

    print(init.postorderTraversal(root))
