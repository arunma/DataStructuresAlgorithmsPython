from collections import defaultdict

from TreeNode import TreeNode


class PathSumIII:
    def pathSum(self, root, target):
        cache = defaultdict(int)
        cache[0] = 1
        self.result = 0
        self.pathSumInner(root, target, cache, currSum=0)
        return self.result

    def pathSumInner(self, node, target, cache, currSum):
        if not node:
            return
        else:
            complement = node.val + currSum - target
            if complement in cache:
                self.result += cache[complement]
            cache[currSum + node.val] += 1
            self.pathSumInner(node.left, target, cache, currSum + node.val)
            self.pathSumInner(node.right, target, cache, currSum + node.val)
            cache[currSum + node.val] -= 1


#
# def pathSumInner(self, node, target, cache, currSum):
#     if node:
#         complement = currSum + node.val - target
#         self.result += cache[complement]
#         cache[currSum + node.val] += 1
#         self.pathSumInner(node.left, target, cache, currSum + node.val)
#         self.pathSumInner(node.right, target, cache, currSum + node.val)
#         cache[currSum + node.val] -= 1
#     return
#
# def pathSum(self, root: TreeNode, sum: int) -> int:
#     cache = defaultdict(int)
#     cache[0] = 1
#     self.result=0
#     self.pathSumInner(root, sum, cache, 0)
#     return self.result


if __name__ == '__main__':
    init = PathSumIII()
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)

    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)

    print(init.pathSum(root, 8))  # 3
