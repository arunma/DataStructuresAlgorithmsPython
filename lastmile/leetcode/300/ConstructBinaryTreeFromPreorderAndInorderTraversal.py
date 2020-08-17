from typing import List

from TreeNode import TreeNode


class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            root_index = inorder.index(root_val)

            root.left = self.buildTree(preorder, inorder[:root_index])
            root.right = self.buildTree(preorder, inorder[root_index + 1:])
            return root


if __name__ == '__main__':
    init = ConstructBinaryTreeFromPreorderAndInorderTraversal()
    print(init.buildTree([3,9,20,15,7], [9,3,15,20,7]))
