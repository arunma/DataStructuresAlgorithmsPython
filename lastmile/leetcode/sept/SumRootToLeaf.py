from TreeNode import TreeNode


class SumRootToLeaf:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = []
        self.helper(root, result, "")

        return sum(int(each, 2) for each in result)

    def helper(self, node, result, curr):

        if not node.left and not node.right:
            result.append(curr + str(node.val))

        if node.left:
            self.helper(node.left, result, curr + str(node.val))

        if node.right:
            self.helper(node.right, result, curr + str(node.val))




if __name__ == '__main__':
    init = SumRootToLeaf()
    r2 = TreeNode(1)
    r2.left = TreeNode(0)
    r2.right = TreeNode(1)
    r2.left.left = TreeNode(0)
    r2.left.right = TreeNode(1)
    r2.right.left = TreeNode(0)
    r2.right.right = TreeNode(1)

    print(init.sumRootToLeaf(r2))
