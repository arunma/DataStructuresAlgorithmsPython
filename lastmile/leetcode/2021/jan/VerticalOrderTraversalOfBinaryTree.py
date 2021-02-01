import sys
from collections import defaultdict
from typing import List

from TreeNode import TreeNode


class VerticalOrderTraversalOfBinaryTree:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        nodeDict=defaultdict(list)

        queue=[(root, 0, 0)]
        minLeft=sys.maxsize
        maxRight=-sys.maxsize

        while queue:
            node, width, height=queue.pop(0)
            minLeft=min(minLeft, width)
            maxRight=max(maxRight, width)

            nodeDict[width].append((height, node.val))
            if node.left:
                queue.append((node.left, width-1, height+1))
            if node.right:
                queue.append((node.right, width+1, height+1))

        result=[]
        for i in range(minLeft, maxRight+1):
            result.append([value for height, value in sorted(nodeDict[i])])

        return result


if __name__ == '__main__':
    init = VerticalOrderTraversalOfBinaryTree()
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    #print(init.verticalTraversal(root1))

    root = TreeNode(0)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)

    root.right.left = TreeNode(2)
    root.right.left.right = TreeNode(3)
    root.right.left.right.right = TreeNode(8)
    root.right.left.right.left = TreeNode(4)
    root.right.left.right.left.left = TreeNode(6)
    root.right.left.right.left.left.left = TreeNode(7)
    print(init.verticalTraversal(root))
