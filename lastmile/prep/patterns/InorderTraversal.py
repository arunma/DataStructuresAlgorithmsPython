from TreeNode import TreeNode


class InorderTraversal:
    def inorderTraversal(self, root):
        stack, result=[],[]
        node=root
        while node or stack:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                result.append(node.val)
                node=node.right
        return result




if __name__ == '__main__':
    init = InorderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(init.inorderTraversal(root))  # [1, 3, 2]
