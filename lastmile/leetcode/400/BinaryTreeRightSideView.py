from typing import List

from TreeNode import TreeNode


class BinaryTreeRightSideView:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            levelCount = len(queue)
            for i in range(levelCount):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return result

    def leftSideView(self, root: TreeNode) -> List[int]:
        print (root)
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            levelCount = len(queue)
            for i in range(levelCount):
                node = queue.pop(0)
                if i == 0:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


if __name__ == '__main__':
    init = BinaryTreeRightSideView()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    print(init.rightSideView(root)) #4,7,6
    print(init.leftSideView(root)) #4,2,1
