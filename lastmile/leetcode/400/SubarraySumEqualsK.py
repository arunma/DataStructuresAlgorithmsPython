from collections import defaultdict
from typing import List


class SubarraySumEqualsK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0]=1
        result = 0
        currSum = 0
        for num in nums:
            currSum += num
            result += prefixSum[currSum - k]
            prefixSum[currSum] += 1

        return result


if __name__ == '__main__':
    init = SubarraySumEqualsK()
    print(init.subarraySum([1, 1, 1], 2))  # 2
