from typing import List

from TreeNode import TreeNode


class BinaryTreePreOrderTraveral:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []

        result = []
        while stack or node:
            if node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return result


if __name__ == '__main__':
    init = BinaryTreePreOrderTraveral()
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.right = TreeNode(6)
    print(init.preorderTraversal(root))
