from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, depth=5):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.val)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


class BinaryTreeZigzagOrderTraversal:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = []
        if not root:
            return queue
        forward = True
        queue.append(root)
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                node = queue.pop(0)
                if forward:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            forward = not forward
            result.append(level)

        return result


if __name__ == '__main__':
    init = BinaryTreeZigzagOrderTraversal()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(init.zigzagLevelOrder(root))
