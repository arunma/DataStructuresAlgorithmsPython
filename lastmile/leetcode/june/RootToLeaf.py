from TreeNode import TreeNode


class RootToLeaf:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        sum=[0]
        self.sumNumbersInner(root, 0, sum)
        return sum[0]

    def sumNumbersInner(self, node, curr_value, sum):
        if not node.right and not node.left:
            sum[0] += curr_value * 10 + node.val
        else:
            if node.left:
                self.sumNumbersInner(node.left, curr_value * 10 + node.val, sum)
            if node.right:
                self.sumNumbersInner(node.right, curr_value * 10 + node.val, sum)


if __name__ == '__main__':
    init = RootToLeaf()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(init.sumNumbers(root1))

    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    print(init.sumNumbers(root2))

    root3 = TreeNode(0)
    root3.left = TreeNode(1)
    print(init.sumNumbers(root3))
