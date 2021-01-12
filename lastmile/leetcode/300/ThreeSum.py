from typing import List


class ThreeSum:
    # def threeSum(self, nums):
    #     nums.sort()
    #     N = len(nums)
    #     result = set()
    #     for i in range(N - 2):
    #         self.two_sum(result, nums, -nums[i], i + 1, N - 1)
    #
    #     return [list(each) for each in result]
    #
    # def two_sum(self, result, nums, target, start, end):
    #     while start < end:
    #         out = nums[start] + nums[end]
    #         if out == target:
    #             result.add(tuple([-target, nums[start], nums[end]]))
    #             start += 1
    #             end -= 1
    #         elif out < target:
    #             start += 1
    #         else:
    #             end -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        result = set()
        for i in range(N - 2):
            self.twoSum(nums, result, -nums[i], i + 1, N - 1)
        return list(map(list, result))

    def twoSum(self, nums, result, target, low, high):
        while low < high:
            curr = nums[low] + nums[high]
            if curr < target:
                low += 1
            elif curr > target:
                high -= 1
            else:
                result.add((-target, nums[low], nums[high]))
                low += 1
                high -= 1


if __name__ == '__main__':
    init = ThreeSum()
    print(init.threeSum([-1, 0, 1, 2, -1, -4]))
    print(init.threeSum([-1, 0, 1, -1]))
    '''
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    '''
