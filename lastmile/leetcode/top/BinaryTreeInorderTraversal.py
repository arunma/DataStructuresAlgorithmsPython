class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeInorderTraversal:

    def inorderTraversalInner(self, root, list):
        if (root is None):
            return
        if (root.left is not None):
            self.inorderTraversalInner(root.left, list)
        list.append(root.val)
        if (root.right is not None):
            self.inorderTraversalInner(root.right, list)

    def inorderTraversal(self, root):
        collect=[]
        self.inorderTraversalInner(root, collect)
        return collect


if __name__ == '__main__':
    init = BinaryTreeInorderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print (init.inorderTraversal(root))
