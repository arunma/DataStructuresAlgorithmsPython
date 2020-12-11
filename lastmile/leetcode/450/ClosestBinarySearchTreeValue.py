from TreeNode import TreeNode


class ClosestBinarySearchTreeValue:
    def closestValue(self, root, target):
        def helper(node, target):
            if not node:
                return
            if abs(node.val - target) < abs(self.closest - target):
                self.closest = node.val

            if target < node.val:
                return helper(node.left, target)
            else:
                return helper(node.right, target)

        self.closest = float('-inf')
        helper(root, target)
        return self.closest


if __name__ == '__main__':
    init = ClosestBinarySearchTreeValue()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(init.closestValue(root, 3.714))
