from TreeNode import TreeNode


class SmalestSubtreeWithAllDeepestNodes:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deep(node):
            if not node:
                return 0, None
            ld = deep(node.left)
            rd = deep(node.right)

            if ld[0] > rd[0]:
                return ld[0] + 1, ld[1]
            elif rd[0] > ld[0]:
                return rd[0] + 1, rd[1]
            else:
                return ld[0] + 1, node
        return deep(root)[1]


if __name__ == '__main__':
    init = SmalestSubtreeWithAllDeepestNodes()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print(init.subtreeWithAllDeepest(root))
