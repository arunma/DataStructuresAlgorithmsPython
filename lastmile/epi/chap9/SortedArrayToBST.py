from typing import List

from TreeNode import TreeNode


class SortedArrayToBST:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.constructTree(nums, 0, len(nums) - 1)

    def constructTree(self, nums, low, high):
        if low > high:
            return None

        mid = low + (high - low) // 2
        node = TreeNode(nums[mid])
        node.left = self.constructTree(nums, 0, mid-1)
        node.right = self.constructTree(nums, mid+1, high)
        return node


if __name__ == '__main__':
    init = SortedArrayToBST()
    print(init.sortedArrayToBST([-10, -3, 0, 5, 9]))
