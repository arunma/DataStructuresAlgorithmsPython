import sys
from collections import defaultdict
from typing import List

from TreeNode import TreeNode


class VerticalOrderTraversalOfABinaryTree:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        self.minWidth = sys.maxsize
        self.maxWidth = -sys.maxsize

        ldict = defaultdict(list)

        def traverse(node, width, height):
            self.minWidth = min(width, self.minWidth)
            self.maxWidth = max(width, self.maxWidth)

            ldict[width].append((height, node.val))
            if node.left:
                traverse(node.left, width - 1, height + 1)

            if node.right:
                traverse(node.right, width + 1, height + 1)

        traverse(root, 0, 0)
        result = []
        for i in range(self.minWidth, self.maxWidth + 1):
            result.append([vals for w, vals in sorted(ldict[i])])

        return result


if __name__ == '__main__':
    init = VerticalOrderTraversalOfABinaryTree()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(init.verticalTraversal(root))
