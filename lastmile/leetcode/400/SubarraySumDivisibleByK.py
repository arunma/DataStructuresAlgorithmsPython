from collections import defaultdict
from typing import List


class SubarraySumDivisibleByK:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1

        currSum = 0
        result = 0
        for num in A:
            currSum += num
            result += prefixSum[currSum % K]

            prefixSum[currSum % K] += 1

        return result


if __name__ == '__main__':
    init = SubarraySumDivisibleByK()
    print(init.subarraysDivByK(A=[4, 5, 0, -2, -3, 1], K=5))
