import sys
from typing import List


class MaximumProductSubarray:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        min_prod=nums[0]
        result=nums[0]
        for i in range(1, len(nums)):
            num=nums[i]
            curr_max=max(num, num*max_prod, num*min_prod)
            min_prod=min(num, num*min_prod, num*max_prod)

            max_prod=curr_max
            result=max(max_prod, result)
        return result






if __name__ == '__main__':
    init = MaximumProductSubarray()
    print(init.maxProduct([2, 3, -2, 4])) #6
    print(init.maxProduct([-2, 0, -1])) #0
    print(init.maxProduct([-2])) #-2
    print(init.maxProduct([0,2])) #2
