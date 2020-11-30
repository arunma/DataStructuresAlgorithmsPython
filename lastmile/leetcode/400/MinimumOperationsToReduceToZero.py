import sys
from typing import List


class MinimumOperationsToReduceToZero:
    def minOperations(self, nums: List[int], x: int) -> int:
        self.count = -sys.maxsize
        self.memo={}
        self.backTrack(nums, x)
        if self.count == -sys.maxsize:
            return -1
        else:
            return len(nums) - self.count

    def backTrack(self, nums, x):
        left = 0
        right = len(nums) - 1
        if tuple(nums) in self.memo:
            return False
        else:
            if x == 0:
                self.count = max(self.count, len(nums))
                return False
            elif x < 0:
                return False

            while left <= right:
                if nums[left] > x and nums[right] > x:
                    return False
                return self.backTrack(nums[1:], x - nums[0]) or self.backTrack(nums[:-1], x - nums[-1])
        self.memo[tuple(nums)]=False
        return False


if __name__ == '__main__':
    init = MinimumOperationsToReduceToZero()
    print(init.minOperations([1, 1, 4, 2, 3], 5))
    print(init.minOperations([5, 6, 7, 8, 9], x=4))
    print(init.minOperations([5, 2, 3, 1, 1], x=5)) #1
