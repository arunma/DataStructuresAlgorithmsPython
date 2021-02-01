from TreeNode import TreeNode

class InorderSuccessortOfBST:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack=[]
        node=root
        found=False
        while node or stack:
            if node:
                stack.append(node)
                node=node.left
            else:
                node=stack.pop()
                if node==p:
                    found=True
                elif found:
                    return node
                node=node.right
        return None



if __name__ == '__main__':
    init = InorderSuccessortOfBST()
    r2 = TreeNode(2)
    r2.left = TreeNode(1)
    r2.right = TreeNode(3)
    print(init.inorderSuccessor(r2, r2.left)) #2

    r2 = TreeNode(5)
    r2.left = TreeNode(3)
    r2.right = TreeNode(6)
    r2.left.left = TreeNode(2)
    r2.left.right = TreeNode(4)
    r2.left.left.left = TreeNode(1)
    print(init.inorderSuccessor(r2, r2.right)) #None
