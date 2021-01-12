import sys

from BinaryTreeInorderTraversal import TreeNode


class ValidateBinarySearchTree:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTInner(root, -sys.maxsize, sys.maxsize)

    def isValidBSTInner(self, root, minval, maxval):
        if not root:
            return True
        val = root.val
        if not minval < val < maxval:
            return False
        return self.isValidBSTInner(root.left, minval, root.val) and self.isValidBSTInner(root.right, root.val, maxval)

if __name__ == '__main__':
    init = ValidateBinarySearchTree()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(init.isValidBST(root))  # true
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(init.isValidBST(root))  # false
