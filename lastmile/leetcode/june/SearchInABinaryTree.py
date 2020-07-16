from TreeNode import TreeNode


class SearchInABinaryTree:
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None
        elif node.val==val:
            return node
        elif val<node.val:
            return self.searchBST(node.left, val)
        else:
            return self.searchBST(node.right, val)



if __name__ == '__main__':
    init = SearchInABinaryTree()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(init.searchBST(root, 2)) #2 1 3
