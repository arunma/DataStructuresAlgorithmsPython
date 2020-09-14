from typing import List


class MinProductSubarray:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        minProduct, maxProduct, result =nums[0], nums[0], nums[0]

        for num in nums[1:]:
            currMax=max(num, minProduct*num, maxProduct*num)
            minProduct=min(num, minProduct*num, maxProduct*num)
            maxProduct=currMax

            result=max(result, maxProduct)
        return result



if __name__ == '__main__':
    init = MinProductSubarray()
    print(init.maxProduct([2,3,-2,4])) #6
    print(init.maxProduct([-2,0,-1])) #0
