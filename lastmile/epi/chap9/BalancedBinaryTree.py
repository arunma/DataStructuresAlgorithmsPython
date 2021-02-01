from TreeNode import TreeNode


class BalancedBinaryTree:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.height(root.left)-self.height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.left), self.height(node.right))

if __name__ == '__main__':
    init = BalancedBinaryTree()
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    print(init.isBalanced(root))

