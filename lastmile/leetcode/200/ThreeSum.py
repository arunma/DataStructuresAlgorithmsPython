from typing import List, Set


class ThreeSum:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        for i in range(0, len(nums) - 1):
            self.searchPair(i + 1, nums, result, -nums[i])
        return [list(each) for each in result]

    def searchPair(self, start, nums, result, target):
        end = len(nums) - 1
        while start < end:
            sum = nums[start] + nums[end]
            if sum == target:
                result.add(tuple([-target, nums[start], nums[end]]))
            if (sum < target):
                start = start + 1
            else:
                end = end - 1


if __name__ == '__main__':
    init = ThreeSum()
    print(init.threeSum([-1, 0, 1, 2, -1, -4]))
    # [
    #     [-1, 0, 1],
    #     [-1, -1, 2]
    # ]
