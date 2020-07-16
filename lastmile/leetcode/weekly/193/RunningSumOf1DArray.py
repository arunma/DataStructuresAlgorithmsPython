from typing import List


class RunningSumOf1DArray:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return []
        n = len(nums)
        result = [0] * n
        result[0]=nums[0]
        for i in range(1, n):
            result[i] = result[i - 1] + nums[i]
        return result


if __name__ == '__main__':
    init = RunningSumOf1DArray()
    print(init.runningSum([3, 1, 2, 10, 1]))
