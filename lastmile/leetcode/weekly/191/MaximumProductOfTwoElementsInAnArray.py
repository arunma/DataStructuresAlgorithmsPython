from typing import List


class MaximumProductOfTwoElementsInAnArray:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


if __name__ == '__main__':
    init = MaximumProductOfTwoElementsInAnArray()
    print(init.maxProduct(nums=[3, 4, 5, 2]))
    print(init.maxProduct(nums=[1, 5, 4, 5]))
