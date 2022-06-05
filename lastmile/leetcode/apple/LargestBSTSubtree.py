import sys
from typing import Optional

from leetcode.commons.TreeNode import TreeNode


class LargestBSTSubtree:
    # def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    #     count, mini, maxi = self.dfs(root)
    #     return count
    #
    # def dfs(self, root):
    #     if not root:
    #         return 0, sys.maxsize, -sys.maxsize
    #
    #     lcount, lmini, lmaxi = self.dfs(root.left)
    #     rcount, rmini, rmaxi = self.dfs(root.right)
    #
    #     if lmaxi<root.val<rmini:
    #         return lcount+rcount+1, min(lmini, root.val), max(rmaxi, root.val)
    #     else:
    #         return max(lcount, rcount), -sys.maxsize, sys.maxsize

    # def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
    #     count, mini, maxi = self.dfs(root)
    #     return count
    #
    # def dfs(self, root):
    #     if not root:
    #         return 0, sys.maxsize, -sys.maxsize
    #
    #     lcount, lmini, lmaxi = self.dfs(root.left)
    #     rcount, rmini, rmaxi = self.dfs(root.right)
    #
    #     if lmaxi < root.val < rmini:
    #         return lcount+rcount+1, min(root.val, lmini), max(root.val, rmaxi)
    #     else:
    #         return max(lcount, rcount), -sys.maxsize, sys.maxsize

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        count, mini, maxi = self.dfs(root)
        return count

    def dfs(self, root):
        if not root:
            return 0, sys.maxsize, -sys.maxsize

        lcount, lmini, lmaxi = self.dfs(root.left)
        rcount, rmini, rmaxi = self.dfs(root.right)

        if lmaxi < root.val < rmini:
            return lcount+rcount+1, min(lmini, root.val), max(rmaxi, root.val)
        else:
            return max(lcount, rcount), -sys.maxsize, sys.maxsize

if __name__ == '__main__':
    init = LargestBSTSubtree()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    print(init.largestBSTSubtree(root))
