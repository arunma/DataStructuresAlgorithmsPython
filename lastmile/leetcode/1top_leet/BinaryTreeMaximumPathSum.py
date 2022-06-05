import sys
from typing import Optional

from leetcode.commons.TreeNode import TreeNode


class BinaryTreeMaximumPathSum:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.maxSum = -sys.maxsize
        self.dfs(root)
        return self.maxSum

    def dfs(self, node):
        if not node:
            return 0
        leftSum = max(self.dfs(node.left), 0)
        rightSum = max(self.dfs(node.right), 0)
        currMax = node.val + leftSum + rightSum
        self.maxSum = max(self.maxSum, currMax)

        return node.val + max(leftSum, rightSum)


if __name__ == '__main__':
    init = BinaryTreeMaximumPathSum()
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(init.maxPathSum(root))  # 42
