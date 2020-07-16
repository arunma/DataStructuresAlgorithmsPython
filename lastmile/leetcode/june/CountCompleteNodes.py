from typing import List

from TreeNode import TreeNode


class CountCompleteNodes:
    def countNodes(self, root: TreeNode) -> int:
        result=[0]
        self.countNodesInner(root, result)
        return result[0]

    def countNodesInner(self, node: TreeNode, result:List[int]):
        if not node:
            return 0
        else:
            result[0] += 1
            self.countNodesInner(node.left, result)
            self.countNodesInner(node.right, result)



if __name__ == '__main__':
    init = CountCompleteNodes()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(init.countNodes(root))  #6
