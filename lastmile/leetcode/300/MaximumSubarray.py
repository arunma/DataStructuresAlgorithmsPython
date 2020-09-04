from typing import List


class MaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            curr_max=max(num, curr_max+num)
            max_sum=max(curr_max, max_sum)
        return max_sum


if __name__ == '__main__':
    init = MaximumSubarray()
    print(init.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
