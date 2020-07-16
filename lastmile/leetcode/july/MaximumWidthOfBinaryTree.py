from TreeNode import TreeNode


class MaximumWidthOfBinaryTree:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [(root, 0)]
        result = 1
        while queue:
            level_size = len(queue)
            _, start = queue[0]
            _, end = queue[-1]
            result = max(result, end - start + 1)
            for _ in range(level_size):
                node, index = queue.pop(0)
                #index=index-start
                if node.left:
                    queue.append((node.left, index*2 + 1))
                if node.right:
                    queue.append((node.right, index*2 + 2))
        return result


if __name__ == '__main__':
    init = MaximumWidthOfBinaryTree()
    r2 = TreeNode(1)
    r2.left = TreeNode(3)
    r2.left.left = TreeNode(5)
    r2.left.right = TreeNode(3)
    print(init.widthOfBinaryTree(r2))  # 2

    r3 = TreeNode(1)
    r3.left = TreeNode(3)
    r3.right = TreeNode(2)
    r3.left.left = TreeNode(5)
    r3.left.right = TreeNode(3)
    r3.right.right = TreeNode(9)
    print(init.widthOfBinaryTree(r3))  # 4
