class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, depth=5):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.val)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


class InvertBinaryTree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        elif root.left is None and root.right is None:
            return root
        else:
            left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            root.left=left
        return root


if __name__ == '__main__':
    init = InvertBinaryTree()
    root=TreeNode(4)
    root.left=TreeNode(2)
    root.right=TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(init.invertTree(root))
