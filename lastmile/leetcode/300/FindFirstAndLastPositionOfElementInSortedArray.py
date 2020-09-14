from typing import List


class FindFirstAndLastPositionOfElementInSortedArray:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     ret = [-1,-1]
    #     for i, num in enumerate(nums):
    #         if num==target and (i==0 or nums[i-1]<num):
    #             ret[0]=i
    #             ret[1]=i
    #         elif num==target and (i==len(nums)-1 or nums[i+1]>num):
    #             ret[1]=i
    #     return ret

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = self.searchForLeft(nums, target)
        right = self.searchForLeft(nums, target+1)

        if left == right:
            return [-1, -1]
        else:
            return [left, right-1]

    def searchForLeft(self, nums, target):
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
