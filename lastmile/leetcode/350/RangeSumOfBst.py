from TreeNode import TreeNode


class RangeSumOfBst:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = []
        node = root

        total = 0

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()

                if L <= node.val <= R:
                    total += node.val

                node = node.right

        return total


if __name__ == '__main__':
    init = RangeSumOfBst()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(init.rangeSumBST(root, 9, 20)) #44
