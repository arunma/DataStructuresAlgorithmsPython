from typing import List

from TreeNode import TreeNode


class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return result

        queue = [root]
        while queue:
            level_size=len(queue)
            level_list=[]
            for i in range(level_size):
                node=queue.pop(0)
                level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_list)
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
