class LowestCommonAncestorOfABinaryTree:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents={root: None}

        queue=[root]
        while p not in parents or q not in parents:
            node=queue.pop(0)

            if node.left:
                parents[node.left]=node
                queue.append(node.left)

            if node.right:
                parents[node.right]=node
                queue.append(node.right)

        ancestors=set()

        while p:
            ancestors.add(p)
            p=parents[p]

        while q not in ancestors:
            q=parents[q]

        return q



if __name__ == '__main__':
    init = LowestCommonAncestorOfABinaryTree()
