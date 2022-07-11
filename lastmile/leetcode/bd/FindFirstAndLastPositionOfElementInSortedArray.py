from typing import List


class FindFirstAndLastPositionOfElementInSortedArray:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = self.binsearch(nums, target)
        right = self.binsearch(nums, target + 1)

        if left==right:
            return [-1,-1]

        return [left, right - 1]

    # def binsearch(self, nums, target, low, high):
    #     low = 0
    #     high = len(nums) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] >= target:
    #             high = mid - 1
    #         else:
    #             low = mid + 1
    #     return low

    def binsearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    init = FindFirstAndLastPositionOfElementInSortedArray()
    print(init.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
    print(init.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
