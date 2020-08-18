from typing import List


class FindPeakElement:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        for i in range(N - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1  # Rising slope


if __name__ == '__main__':
    init = FindPeakElement()
    print(init.findPeakElement([1, 2, 3, 1]))  # 2
    print(init.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 1 or 5
    print(init.findPeakElement([2, 1]))  # 0
    print(init.findPeakElement([1]))  # 0
    print(init.findPeakElement([1, 2]))  # 1
