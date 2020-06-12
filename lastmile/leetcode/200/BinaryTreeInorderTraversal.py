from typing import List


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
        ret += "\n" + ("    " * depth) + str(self.val)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []

        def inorderTraversalInner(node, result):
            if node.left:
                inorderTraversalInner(node.left, result)
            result.append(node.val)
            if node.right:
                inorderTraversalInner(node.right, result)

        inorderTraversalInner(root, result)
        return result


if __name__ == '__main__':
    init = BinaryTreeInorderTraversal()
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(root)
    print(init.inorderTraversal(root))
