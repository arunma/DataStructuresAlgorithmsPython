from typing import List

from leetcode.commons.TreeNode import TreeNode


class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root=preorder.pop(0)
            node=TreeNode(root)
            rindex=inorder.index(root)
            node.left=self.buildTree(preorder, inorder[:rindex])
            node.right=self.buildTree(preorder, inorder[rindex+1:])
            return node


if __name__ == '__main__':
    init = ConstructBinaryTreeFromPreorderAndInorderTraversal()
    print(init.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
