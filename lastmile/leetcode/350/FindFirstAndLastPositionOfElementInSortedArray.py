from typing import List


class FindFirstAndLastPositionOfElementInSortedArray:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ltarget = target - 0.5
        rtarget = target + 0.5

        left=self.binSearch(nums, ltarget)
        right=self.binSearch(nums, rtarget)

        if left==right:
            return [-1,-1]
        else:
            return [left, right-1]

    def binSearch(self, nums, target):
        low, high=0, len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return low


if __name__ == '__main__':
    init = FindFirstAndLastPositionOfElementInSortedArray()
    print(init.searchRange(nums=[1], target=1))  # [3,4
    print(init.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4
    print(init.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
