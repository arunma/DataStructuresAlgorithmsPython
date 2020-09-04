import heapq

from TreeNode import TreeNode


class KthSmallestInBST:
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     stack = []
    #     while root or stack:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root=stack.pop()
    #         k -= 1
    #         if k == 0:
    #             return root.val
    #         root = root.right
    #
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     travers = self.inorder_traversal(root)
    #     return travers[k-1]
    #
    # def inorder_traversal(self, root):
    #     return self.inorder_traversal(root.left) + [root.val] + self.inorder_traversal(root.right) if root else []
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        pq=[]
        queue=[root]
        while queue:
            node=queue.pop(0)
            heapq.heappush(pq, -node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if len(pq)>k:
                heapq.heappop(pq)

        return -pq[0]


if __name__ == '__main__':
    init = KthSmallestInBST()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(init.kthSmallest(root, 1))  # 1

    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(2)
    root1.left.right = TreeNode(4)
    root1.left.left.left = TreeNode(1)
    print(init.kthSmallest(root1, 3))  # 3

    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(init.kthSmallest(root2, 2))  # 2
