import collections
from typing import List

from TreeNode import TreeNode


class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue=collections.deque([root])
        result=[]

        while queue:
            temp=[]
            for i in range(len(queue)):
                node=queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(temp)
        return result


if __name__ == '__main__':
    init = BinaryTreeLevelOrderTraversal()
