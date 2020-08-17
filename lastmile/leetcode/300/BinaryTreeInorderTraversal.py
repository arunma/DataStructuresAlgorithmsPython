from typing import List

from TreeNode import TreeNode


class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        self.inorderTraversalInner(root, result)
        return result

    def inorderTraversalInner(self, node, result):
        if not node:
            return
        if node.left:
            self.inorderTraversalInner(node.left, result)
        result.append(node.val)
        if node.right:
            self.inorderTraversalInner(node.right, result)



if __name__ == '__main__':
    init = BinaryTreeInorderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(init.inorderTraversal(root))
