import collections
from collections import deque

from TreeNode import TreeNode


class InvertABinaryTree:

    def invertTree(self, root):
        if not root:
            return root
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left, root.right = right, left
            return root

    # def invertTree(self, root):
    #     if root:
    #         root.left, root.right=self.invertTree(root.right), self.invertTree(root.left)
    #         return root

    def invertTreeStack(self, root):
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            else:
                node.left, node.right=node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root



if __name__ == '__main__':
    init = InvertABinaryTree()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(init.invertTreeStack(root))
