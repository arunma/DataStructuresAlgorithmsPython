import sys
from typing import List

from BinaryTreeInorderTraversal import TreeNode


class FindLargestValueInEachTreeRow:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]

        result = []
        while queue:
            level_max = -sys.maxsize
            for i in range(len(queue)):
                curr = queue.pop(0)
                level_max = max(level_max, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(level_max)

        return result


if __name__ == '__main__':
    init = FindLargestValueInEachTreeRow()
