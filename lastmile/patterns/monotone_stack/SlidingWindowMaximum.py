import collections
from collections import deque
from typing import List


class SlidingWindowMaximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        stack=[]
        result=[]

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]]<num:
                stack.pop()
            stack.append(i)

            if stack and stack[0]<=i-k:
                stack.pop(0)

            if i>=k-1:
                result.append(nums[stack[0]])

        return result

if __name__ == '__main__':
    init = SlidingWindowMaximum()
    print(init.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(init.maxSlidingWindow(nums = [1,-1], k = 1))
