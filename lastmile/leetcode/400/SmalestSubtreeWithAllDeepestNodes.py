from TreeNode import TreeNode


class SmalestSubtreeWithAllDeepestNodes:
    # def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    #     def deep(node):
    #         if not node:
    #             return 0, None
    #         ld = deep(node.left)
    #         rd = deep(node.right)
    #
    #         if ld[0] > rd[0]:
    #             return ld[0] + 1, ld[1]
    #         elif rd[0] > ld[0]:
    #             return rd[0] + 1, rd[1]
    #         else:
    #             return ld[0] + 1, node
    #     return deep(root)[1]

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.getDeepTree(root)[1]

    def getDeepTree(self, node):
        if not node:
            return (0, None)

        left = self.getDeepTree(node.left)
        right = self.getDeepTree(node.right)

        if left[0] > right[0]:
            return (left[0] + 1, left[1])
        elif right[0] > left[0]:
            return (right[0] + 1, right[1])
        else:
            return (left[0] + 1, node)


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
