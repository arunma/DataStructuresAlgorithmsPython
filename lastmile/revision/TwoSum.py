from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = defaultdict(int)

        for i, num in enumerate(nums):
            exp = target - num
            if exp in sum_map:
                return [sum_map[exp], i]
            else:
                sum_map[num] = i
        return [-1, -1]

