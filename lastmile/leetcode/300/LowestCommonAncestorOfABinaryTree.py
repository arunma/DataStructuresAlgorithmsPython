from TreeNode import TreeNode


class LowestCommonAncestorOfABinaryTree:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        stack=[root]
        parent={root:None}

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left]=node
            if node.right:
                stack.append(node.right)
                parent[node.right]=node

        ancestors=set()
        while p:
            ancestors.add(p)
            p=parent[p]

        while q not in ancestors:
            q=parent[q]

        return q




if __name__ == '__main__':
    init = LowestCommonAncestorOfABinaryTree()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    print(init.lowestCommonAncestor(root, root.left, root.right))
