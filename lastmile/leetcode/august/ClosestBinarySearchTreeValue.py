from TreeNode import TreeNode


class ClosestBinarySearchTreeValue:
    # def closestValue(self, root: TreeNode, target: float) -> int:
    #     def inorder(node):
    #         if not node:
    #             return []
    #         else:
    #             return inorder(node.left) + [node.val] + inorder(node.right)
    #
    #     return min(inorder(root), key = lambda x: abs(target-x))

    def closestValue(self, root: TreeNode, target: float) -> int:
        self.result = float('inf')

        def helper(node, target):
            if not node:
                return
            if abs(node.val - target) < abs(self.result - target):
                self.result = node.val

            if target<node.val:
                helper(node.left, target)

            if target>node.val:
                helper(node.right, target)

        helper(root, target)
        return self.result


if __name__ == '__main__':
    init = ClosestBinarySearchTreeValue()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(init.closestValue(root, 3.714286))
