import collections
from typing import List

from TreeNode import TreeNode


class LevelOrderTraversal:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return result

        queue = collections.deque()
        queue.append(root)
        while queue:
            N=len(queue)
            curr_list=[]
            for i in range(N):
                curr=queue.popleft()
                curr_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.insert(0, curr_list)
        return result


if __name__ == '__main__':
    init = LevelOrderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(init.levelOrderBottom(root))
