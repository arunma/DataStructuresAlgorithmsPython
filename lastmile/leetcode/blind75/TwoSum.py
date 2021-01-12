from collections import defaultdict
from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in sumMap:
                return [sumMap[target - num], i]
            else:
                sumMap[num] = i
        return [-1, -1]


if __name__ == '__main__':
    init = TwoSum()
