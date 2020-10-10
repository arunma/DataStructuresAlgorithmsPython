from typing import List

from TreeNode import TreeNode

class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        node = root

        result = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result


if __name__ == '__main__':
    init = BinaryTreeInorderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(4)
    print(init.inorderTraversal(root))
