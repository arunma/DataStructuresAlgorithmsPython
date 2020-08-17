from typing import List

from TreeNode import TreeNode


class BinaryTreeZigZagLevelOrderTraversal:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return result

        queue=[root]
        left=True
        while queue:
            size=len(queue)
            level_list=[]
            for i in range(size):
                node=queue.pop(0)
                if left:
                    level_list.append(node.val)
                else:
                    level_list.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            left=not left
            result.append(level_list)
        return result

if __name__ == '__main__':
    init = BinaryTreeZigZagLevelOrderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(init.zigzagLevelOrder(root))
