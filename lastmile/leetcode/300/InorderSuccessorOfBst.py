from BinaryTreeInorderTraversal import TreeNode


class InorderSuccessorOfBst:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        succ=None
        while root:
            if p.val<root.val:
                succ=root
                root=root.left
            else:
                root=root.right
        return succ

if __name__ == '__main__':
    init = InorderSuccessorOfBst()
    r2 = TreeNode(2)
    r2.left = TreeNode(1)
    r2.right = TreeNode(3)
    print(init.inorderSuccessor(r2, r2.left)) #2

    r2 = TreeNode(5)
    r2.left = TreeNode(3)
    r2.right = TreeNode(6)
    r2.left.left = TreeNode(2)
    r2.left.right = TreeNode(4)
    r2.left.left.left = TreeNode(1)
    print(init.inorderSuccessor(r2, r2.right)) #None
