class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeInorderTraversal:

    def inorderTraversal(self, root):
        result=[]
        self.inorderTraversalHelper(root, result)
        return result

    def inorderTraversalHelper(self, node, result):
        if not node:
            return
        self.inorderTraversalHelper(node.left, result)
        result.append(node.val)
        self.inorderTraversalHelper(node.right, result)


# def inorderTraversalInner(self, root, list):
    #     if (root is None):
    #         return
    #     if (root.left is not None):
    #         self.inorderTraversalInner(root.left, list)
    #     list.append(root.val)
    #     if (root.right is not None):
    #         self.inorderTraversalInner(root.right, list)
    #
    # def inorderTraversal(self, root):
    #     collect=[]
    #     self.inorderTraversalInner(root, collect)
    #     return collect

    # def inorderTraversal(self, root):
    #     stack,result=[],[]
    #
    #     while True:
    #         while root:
    #             stack.append(root)
    #             root=root.left
    #
    #         if not stack:
    #             return result
    #
    #         curr=stack.pop()
    #         result.append(curr.val)
    #         root=curr.right
    #
    #     return result


    # def inorderTraversal(self, root):
    #     stack,result=[],[]
    #     node=root
    #     while node or stack:
    #         if node:
    #             stack.append(node)
    #             node=node.left
    #         else:
    #             node=stack.pop()
    #             result.append(node.val)
    #             node=node.right
    #     return result






if __name__ == '__main__':
    init = BinaryTreeInorderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print (init.inorderTraversal(root)) #[1, 3, 2]
