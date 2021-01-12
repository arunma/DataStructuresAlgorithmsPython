from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueMap = {}

        for i, num in enumerate(nums):
            if target - num in valueMap:
                return [i, valueMap[target - num]]
            else:
                valueMap[num] = i
        return [-1, -1]

if __name__ == '__main__':
    init = TwoSum()
