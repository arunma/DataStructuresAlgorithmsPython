from TreeNode import TreeNode


class LowestCommonAncestorOfBinarySearchTree:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val>p.val and root.val>q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
            else:
                return root

if __name__ == '__main__':
    init = LowestCommonAncestorOfBinarySearchTree()
