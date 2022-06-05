from typing import List

from leetcode.commons.TreeNode import TreeNode


class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]

        queue=[root]

        while queue:
            currlist=[]
            for i in range(len(queue)):
                curr=queue.pop(0)
                currlist.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(currlist)
        return result







if __name__ == '__main__':
    init = BinaryTreeLevelOrderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(init.levelOrder(root))
    '''
    [
  [3],
  [9,20],
  [15,7]
]
    '''
