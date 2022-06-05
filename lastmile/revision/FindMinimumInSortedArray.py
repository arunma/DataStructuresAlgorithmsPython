import sys
from typing import List


class FindMinimumInSortedArray:
    def findMin(self, nums: List[int]) -> int:
        N=len(nums)
        low=0
        high=N-1

        resmin=sys.maxsize

        while low<=high:
            mid=low+(high-low)//2
            #Did the rotation happen before or after the mid
            if nums[mid]<=nums[high]:
                high = mid - 1
            else:
                low = mid + 1
            resmin=min(resmin,nums[mid])
        return resmin




if __name__ == '__main__':
    init = FindMinimumInSortedArray()
    print(init.findMin(nums = [3,4,5,1,2])) #1
    print(init.findMin(nums = [4,5,6,7,0,1,2])) #0
    print(init.findMin(nums = [11,13,15,17])) #11
