from typing import List


class RemoveDuplicates:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return -1
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


if __name__ == '__main__':
    init = RemoveDuplicates()
    print(init.removeDuplicates([1, 1, 2]))
    print(init.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
