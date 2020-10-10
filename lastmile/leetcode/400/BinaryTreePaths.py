from typing import List

from TreeNode import TreeNode


class BinaryTreePaths:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        queue = [(root, str(root.val))]

        result = []
        while queue:
            node, path = queue.pop(0)

            if not node.left and not node.right:
                result.append(path)

            if node.left:
                npath = path + '->' + str(node.left.val)
                queue.append((node.left, npath))
            if node.right:
                npath = path + '->' + str(node.right.val)
                queue.append((node.right, npath))

        return result


if __name__ == '__main__':
    init = BinaryTreePaths()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)

    print(init.binaryTreePaths(root))
