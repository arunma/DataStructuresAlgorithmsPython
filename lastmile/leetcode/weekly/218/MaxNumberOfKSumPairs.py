from collections import defaultdict
from typing import List


class MaxNumberOfKSumPairs:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        nums.sort()
        count = 0

        low = 0
        high = len(nums) - 1

        while low < high:
            if nums[low] + nums[high] == k:
                count += 1
                low += 1
                high -= 1
            elif nums[low]+nums[high]<k:
                low+=1
            else:
                high-=1
        return count



if __name__ == '__main__':
    init = MaxNumberOfKSumPairs()
    print(init.maxOperations(nums=[1, 2, 3, 4], k=5))
    print(init.maxOperations(nums=[3, 1, 3, 4, 3], k=6))
