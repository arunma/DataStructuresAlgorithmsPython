from typing import List


class SearchInsertPosition:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    init = SearchInsertPosition()
    print(init.searchInsert([1, 3, 5, 6], 5))  # 2
    print(init.searchInsert([1, 3, 5, 6], 2))  # 1
    print(init.searchInsert([1, 3, 5, 6], 7))  # 4
    print(init.searchInsert([1, 3, 5, 6], 0))  # 0
